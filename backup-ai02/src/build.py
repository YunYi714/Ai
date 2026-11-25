"""產生靜態網站到 ../docs。用法：python3 build.py"""
import importlib, json, pathlib, shutil, html
from config import *
ROOT = pathlib.Path(__file__).parent
OUT = ROOT.parent / "docs"
def load(d): return sorted((importlib.import_module(f"{d}.{p.stem}") for p in (ROOT/d).glob("*.py") if not p.stem.startswith("_")), key=lambda m: m.ORDER)
tools = load("tools"); guides = load("guides")
TMAP = {t.SLUG: t for t in tools}

def adsense_head():
    return f'<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={ADSENSE_CLIENT}" crossorigin="anonymous"></script>' if ADSENSE_CLIENT else ""
def ad_slot():
    # 開啟 AdSense「自動廣告」時不需要手動放廣告位；這裡保留一個位置
    return '<div class="ad"></div>'

def page(path, title, desc, body, jsonld=None, extra_js=""):
    url = f"{SITE_URL}/{path}".replace("/index.html", "/")
    ld = "".join(f'<script type="application/ld+json">{json.dumps(j, ensure_ascii=False)}</script>' for j in (jsonld or []))
    nav = '<a href="rent-checkup.html">租屋健檢</a><a href="rights.html">權益懶人包</a><a href="how-to-claim-rights.html">爭取權益</a><a href="./#tools">計算工具</a>' 
    doc = f'''<!DOCTYPE html><html lang="zh-Hant-TW"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{url}"><meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}">
<meta property="og:type" content="website"><meta property="og:url" content="{url}"><meta property="og:locale" content="zh_TW">
<link rel="stylesheet" href="assets/style.css">{adsense_head()}{ld}</head><body>
<header><a href="./">🧮 {SITE_NAME}</a><nav>{nav}</nav></header>
<main>{body}</main>
<footer>© 2026 {SITE_NAME}｜{SITE_TAGLINE}<br><a href="about.html">關於本站</a><a href="privacy.html">隱私權政策</a><a href="contact.html">聯絡我們</a>
<p>本站計算結果僅供參考，不構成法律或財務建議，實際權益請以主管機關解釋為準。</p></footer>
<script src="assets/common.js"></script>{extra_js}</body></html>'''
    (OUT/path).write_text(doc, encoding="utf-8")

def rights_box(t):
    gs = [g for g in guides if t.SLUG in getattr(g, "TOOLS", [])]
    links = "".join(f'<li><a href="{g.SLUG}.html">{g.TITLE}</a></li>' for g in gs)
    return f'<div class="card" style="border-color:#e0a800;background:#fffaf0"><b>⚠️ 覺得被房東坑了？</b><ul>{links}<li><a href="how-to-claim-rights.html"><b>爭取權益的方法：蒐證、申訴、調解</b></a></li></ul></div>'

def guide_pages():
    for g in guides:
        parts = [f'<h1>{g.TITLE}</h1><p class="lead">{g.SHORT}</p>']
        if g.RULES: parts.append(f'<h2>法律怎麼規定？</h2>{g.RULES}')
        if g.MYTHS: parts.append('<h2>房東常見的說法 vs. 真正的規定</h2>' + "".join(f'<div class="card"><b>❌ 「{m}」</b><p style="margin:.4em 0 0">✅ {t}</p></div>' for m, t in g.MYTHS))
        parts.append(ad_slot())
        parts.append(('<h2>爭取權益的方法</h2>' if g.RULES else '') + g.ACTIONS)
        if g.RULES: parts.append('<p>👉 完整流程與訊息範本：<a href="how-to-claim-rights.html">爭取權益的方法</a></p>')
        if g.FAQ: parts.append('<h2>常見問題</h2>' + "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in g.FAQ))
        rel = "".join(f'<a href="{TMAP[s].SLUG}.html"><b>{TMAP[s].TITLE}</b><span>{TMAP[s].SHORT}</span></a>' for s in g.TOOLS)
        others = "".join(f'<li><a href="{o.SLUG}.html">{o.TITLE}</a></li>' for o in guides if o is not g)
        parts.append(f'<p class="note">最後更新：{UPDATED}。本文為法規整理，不構成法律意見，個案請洽消保官、地政機關或律師。</p><h2>相關工具</h2><div class="grid">{rel}</div><h2>其他權益懶人包</h2><ul>{others}</ul>')
        ld = [{"@context":"https://schema.org","@type":"Article","headline":g.TITLE,"description":g.DESC,"inLanguage":"zh-TW","dateModified":UPDATED,"url":f"{SITE_URL}/{g.SLUG}.html"}]
        if g.FAQ: ld.append({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in g.FAQ]})
        page(f"{g.SLUG}.html", f"{g.TITLE}｜{SITE_NAME}", g.DESC, "".join(parts), ld)
    cards = "".join(f'<a href="{g.SLUG}.html"><b>{g.TITLE}</b><span>{g.SHORT}</span></a>' for g in guides)
    page("rights.html", f"租屋權益懶人包：押金、電費、報稅、修繕、提前解約｜{SITE_NAME}", "租屋族必看的權益懶人包：每篇整理法律規定、房東常見的違法說法，以及爭取權益的方法。",
         f'<h1>租屋權益懶人包</h1><p class="lead">很多房客不知道自己的權益被侵害了。每篇都整理了法律規定、房東常見的違法說法，以及<b>爭取權益的方法</b>。</p><p><a href="rent-checkup.html"><b>👉 不確定從哪裡看起？先做 3 分鐘租屋權益健檢</b></a></p><div class="grid">{cards}</div>')

def build():
    if OUT.exists(): shutil.rmtree(OUT)
    (OUT/"assets").mkdir(parents=True)
    shutil.copy(ROOT/"style.css", OUT/"assets/style.css"); shutil.copy(ROOT/"common.js", OUT/"assets/common.js")
    (OUT/".nojekyll").write_text("")
    for t in tools:
        faq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in t.FAQ)
        related = "".join(f'<a href="{o.SLUG}.html"><b>{o.TITLE}</b><span>{o.SHORT}</span></a>' for o in tools if o is not t)
        body = f'''<h1>{t.TITLE}</h1><p class="lead">{t.SHORT}</p><div class="card">{t.FORM}</div>{ad_slot()}
{t.ARTICLE}<h2>常見問題</h2>{faq}{rights_box(t)}<p class="note">最後更新：{UPDATED}</p>{ad_slot()}<h2>其他好用工具</h2><div class="grid">{related}</div>'''
        ld = [{"@context":"https://schema.org","@type":"WebApplication","name":t.TITLE,"description":t.DESC,"url":f"{SITE_URL}/{t.SLUG}.html",
               "applicationCategory":"UtilitiesApplication","operatingSystem":"All","inLanguage":"zh-TW","offers":{"@type":"Offer","price":"0","priceCurrency":"TWD"}},
              {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in t.FAQ]}]
        page(f"{t.SLUG}.html", f"{t.TITLE}｜{SITE_NAME}", t.DESC, body, ld, f"<script>{t.JS}</script>")
    guide_pages()
    cards = "".join(f'<a href="{t.SLUG}.html"><b>{t.TITLE}</b><span>{t.SHORT}</span></a>' for t in tools)
    gcards = "".join(f'<a href="{g.SLUG}.html"><b>{g.TITLE}</b><span>{g.SHORT}</span></a>' for g in guides)
    page("index.html", f"{SITE_NAME}｜押金、電費、報稅、修繕，房客權益一次查", f"{SITE_NAME}：{SITE_TAGLINE}。押金最多幾個月、房東電費每度可以收多少、租金報稅可以省多少、提前解約違約金，輸入數字立即檢查。",
         f'<h1>{SITE_NAME}</h1><p class="lead">{SITE_TAGLINE}。押金收 3 個月、電費一度收 6 元、不讓你報稅、東西壞了叫你自己修……很多房客不知道這些可能都違法。這裡幫你查清楚，並教你怎麼爭取。</p>'
         '<div class="card" style="border-color:var(--c)"><b style="font-size:1.15rem">🏠 租屋權益健檢</b><p style="margin:.3em 0">回答 10 個問題，3 分鐘知道房東有沒有違法。簽約前、住進去後都適用。</p><a href="rent-checkup.html"><button>開始健檢</button></a></div>'
         f'<h2 id="tools">計算工具</h2><div class="grid">{cards}</div>{ad_slot()}<h2>租屋權益懶人包</h2><div class="grid">{gcards}</div>'
         '<h2>為什麼做這個網站？</h2><p>台灣有數百萬租屋族，但租屋相關的規定分散在《租賃住宅市場發展及管理條例》、《民法》、內政部的定型化契約規定裡，很難找。這裡把常見問題整理成工具和懶人包，並附上法規依據，讓每個房客都能自己檢查。</p>',
         [{"@context":"https://schema.org","@type":"WebSite","name":SITE_NAME,"url":SITE_URL+"/","inLanguage":"zh-TW"}])
    page("about.html", f"關於本站｜{SITE_NAME}", f"關於{SITE_NAME}", f'<h1>關於本站</h1><p>{SITE_NAME}提供台灣租屋族權益查詢與免費線上試算工具，所有計算都在你的瀏覽器中完成，不會上傳你輸入的任何資料。</p><p>各工具依《租賃住宅市場發展及管理條例》、《民法》、內政部住宅租賃定型化契約應記載及不得記載事項及財政部公告編寫，並附上計算方式與法條說明。法規如有修正，我們會盡快更新。計算結果僅供參考，實際權益請以主管機關解釋為準。</p><p>發現錯誤或想要新的計算工具？歡迎<a href="contact.html">聯絡我們</a>。</p>')
    page("contact.html", f"聯絡我們｜{SITE_NAME}", f"聯絡{SITE_NAME}", '<h1>聯絡我們</h1><p>如發現計算錯誤、法規更新或有任何建議，歡迎來信：</p><p class="big" style="font-size:1.1rem">✉️ <!--CONTACT_EMAIL-->（請在 site_src/build.py 填入聯絡信箱）</p>')
    page("privacy.html", f"隱私權政策｜{SITE_NAME}", f"{SITE_NAME}隱私權政策", f'''<h1>隱私權政策</h1><p>最後更新：{UPDATED}</p>
<h2>我們收集的資料</h2><p>本站所有計算皆在你的瀏覽器中執行，你輸入的薪資、日期、金額等資料<b>不會</b>傳送到我們的伺服器，也不會被儲存。</p>
<h2>Cookie 與廣告</h2><p>本站使用 Google AdSense 等第三方廣告服務。第三方供應商（包括 Google）會使用 Cookie，根據使用者先前造訪本網站或其他網站的紀錄放送廣告。Google 使用廣告 Cookie，可讓 Google 及其合作夥伴根據使用者造訪本站和（或）網路上其他網站的情形，向使用者放送廣告。</p>
<p>你可以前往 <a href="https://adssettings.google.com/" rel="nofollow">Google 廣告設定</a> 停用個人化廣告，或前往 <a href="https://www.aboutads.info/" rel="nofollow">www.aboutads.info</a> 停用第三方供應商的個人化廣告 Cookie。</p>
<h2>流量分析</h2><p>本站可能使用匿名的流量統計工具了解網站使用情況，這些資料不包含可識別個人身分的資訊。</p>
<h2>外部連結</h2><p>本站可能包含其他網站的連結，這些網站的隱私權政策不在本政策範圍內。</p>
<h2>政策修訂</h2><p>本政策如有修訂，將公告於本頁面。如有疑問請<a href="contact.html">聯絡我們</a>。</p>''')
    page("404.html", f"找不到頁面｜{SITE_NAME}", "找不到頁面", f'<h1>找不到這個頁面</h1><p>回到<a href="./">首頁</a>看看所有工具。</p><div class="grid">{cards}</div>')
    urls = [""] + [f"{t.SLUG}.html" for t in tools] + ["rights.html"] + [f"{g.SLUG}.html" for g in guides] + ["about.html", "privacy.html", "contact.html"]
    (OUT/"sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
        "".join(f"<url><loc>{SITE_URL}/{u}</loc><lastmod>{UPDATED}</lastmod></url>\n" for u in urls) + "</urlset>\n")
    (OUT/"robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n")
    if ADSENSE_CLIENT:
        (OUT/"ads.txt").write_text(f"google.com, {ADSENSE_CLIENT.replace('ca-','')}, DIRECT, f08c47fec0942fa0\n")
    print(f"built {len(tools)} tools -> {OUT}")
build()
