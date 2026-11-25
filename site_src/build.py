"""產生靜態網站到 ../docs。用法：python3 build.py"""
import importlib, json, pathlib, shutil, html
from config import *
ROOT = pathlib.Path(__file__).parent
OUT = ROOT.parent / "docs"
tools = sorted((importlib.import_module(f"tools.{p.stem}") for p in (ROOT/"tools").glob("*.py") if not p.stem.startswith("_")), key=lambda m: m.ORDER)

def adsense_head():
    return f'<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={ADSENSE_CLIENT}" crossorigin="anonymous"></script>' if ADSENSE_CLIENT else ""
def ad_slot():
    # 開啟 AdSense「自動廣告」時不需要手動放廣告位；這裡保留一個位置
    return '<div class="ad"></div>'

def page(path, title, desc, body, jsonld=None, extra_js=""):
    url = f"{SITE_URL}/{path}".replace("/index.html", "/")
    ld = "".join(f'<script type="application/ld+json">{json.dumps(j, ensure_ascii=False)}</script>' for j in (jsonld or []))
    nav = "".join(f'<a href="{t.SLUG}.html">{getattr(t,"NAV",t.TITLE.split("（")[0].replace("計算機",""))}</a>' for t in tools[:4])
    doc = f'''<!DOCTYPE html><html lang="zh-Hant-TW"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{url}"><meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}">
<meta property="og:type" content="website"><meta property="og:url" content="{url}"><meta property="og:locale" content="zh_TW">
<link rel="stylesheet" href="assets/style.css">{adsense_head()}{ld}</head><body>
<header><a href="./">🧮 {SITE_NAME}</a><nav>{nav}<a href="./">全部工具</a></nav></header>
<main>{body}</main>
<footer>© 2026 {SITE_NAME}｜{SITE_TAGLINE}<br><a href="about.html">關於本站</a><a href="privacy.html">隱私權政策</a><a href="contact.html">聯絡我們</a>
<p>本站計算結果僅供參考，不構成法律或財務建議，實際權益請以主管機關解釋為準。</p></footer>
<script src="assets/common.js"></script>{extra_js}</body></html>'''
    (OUT/path).write_text(doc, encoding="utf-8")

def build():
    if OUT.exists(): shutil.rmtree(OUT)
    (OUT/"assets").mkdir(parents=True)
    shutil.copy(ROOT/"style.css", OUT/"assets/style.css"); shutil.copy(ROOT/"common.js", OUT/"assets/common.js")
    (OUT/".nojekyll").write_text("")
    for t in tools:
        faq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in t.FAQ)
        related = "".join(f'<a href="{o.SLUG}.html"><b>{o.TITLE}</b><span>{o.SHORT}</span></a>' for o in tools if o is not t)
        body = f'''<h1>{t.TITLE}</h1><p class="lead">{t.SHORT}</p><div class="card">{t.FORM}</div>{ad_slot()}
{t.ARTICLE}<h2>常見問題</h2>{faq}<p class="note">最後更新：{UPDATED}</p>{ad_slot()}<h2>其他好用工具</h2><div class="grid">{related}</div>'''
        ld = [{"@context":"https://schema.org","@type":"WebApplication","name":t.TITLE,"description":t.DESC,"url":f"{SITE_URL}/{t.SLUG}.html",
               "applicationCategory":"FinanceApplication","operatingSystem":"All","inLanguage":"zh-TW","offers":{"@type":"Offer","price":"0","priceCurrency":"TWD"}},
              {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in t.FAQ]}]
        page(f"{t.SLUG}.html", f"{t.TITLE}｜{SITE_NAME}", t.DESC, body, ld, f"<script>{t.JS}</script>")
    cards = "".join(f'<a href="{t.SLUG}.html"><b>{t.TITLE}</b><span>{t.SHORT}</span></a>' for t in tools)
    page("index.html", f"{SITE_NAME}｜加班費、特休、資遣費、房貸、分期利率免費計算", f"{SITE_NAME}：{SITE_TAGLINE}。加班費、特休天數、資遣費、最低工資、房貸、分期付款利率、複利，輸入數字立即算出結果，依台灣最新法規。",
         f'<h1>{SITE_NAME}</h1><p class="lead">{SITE_TAGLINE}。免註冊、免下載，手機也好用，依台灣最新法規計算。</p><div class="grid">{cards}</div>{ad_slot()}'
         '<h2>為什麼做這個網站？</h2><p>勞基法的加班費、特休、資遣費規定其實不難，但條文寫得很繞，很多人不知道自己該拿多少。分期付款、房貸的利率也常常讓人看不清真實成本。這裡把常見的計算做成簡單工具，並附上法條依據與範例，讓每個人都能自己算清楚。</p>',
         [{"@context":"https://schema.org","@type":"WebSite","name":SITE_NAME,"url":SITE_URL+"/","inLanguage":"zh-TW"}])
    page("about.html", f"關於本站｜{SITE_NAME}", f"關於{SITE_NAME}", f'<h1>關於本站</h1><p>{SITE_NAME}提供台灣勞工權益與個人理財的免費線上試算工具，所有計算都在你的瀏覽器中完成，不會上傳你輸入的任何資料。</p><p>各工具依《勞動基準法》、《勞工退休金條例》及勞動部公告編寫，並附上計算方式與法條說明。法規如有修正，我們會盡快更新。計算結果僅供參考，實際權益請以主管機關解釋為準。</p><p>發現錯誤或想要新的計算工具？歡迎<a href="contact.html">聯絡我們</a>。</p>')
    page("contact.html", f"聯絡我們｜{SITE_NAME}", f"聯絡{SITE_NAME}", '<h1>聯絡我們</h1><p>如發現計算錯誤、法規更新或有任何建議，歡迎來信：</p><p class="big" style="font-size:1.1rem">✉️ <!--CONTACT_EMAIL-->（請在 site_src/build.py 填入聯絡信箱）</p>')
    page("privacy.html", f"隱私權政策｜{SITE_NAME}", f"{SITE_NAME}隱私權政策", f'''<h1>隱私權政策</h1><p>最後更新：{UPDATED}</p>
<h2>我們收集的資料</h2><p>本站所有計算皆在你的瀏覽器中執行，你輸入的薪資、日期、金額等資料<b>不會</b>傳送到我們的伺服器，也不會被儲存。</p>
<h2>Cookie 與廣告</h2><p>本站使用 Google AdSense 等第三方廣告服務。第三方供應商（包括 Google）會使用 Cookie，根據使用者先前造訪本網站或其他網站的紀錄放送廣告。Google 使用廣告 Cookie，可讓 Google 及其合作夥伴根據使用者造訪本站和（或）網路上其他網站的情形，向使用者放送廣告。</p>
<p>你可以前往 <a href="https://adssettings.google.com/" rel="nofollow">Google 廣告設定</a> 停用個人化廣告，或前往 <a href="https://www.aboutads.info/" rel="nofollow">www.aboutads.info</a> 停用第三方供應商的個人化廣告 Cookie。</p>
<h2>流量分析</h2><p>本站可能使用匿名的流量統計工具了解網站使用情況，這些資料不包含可識別個人身分的資訊。</p>
<h2>外部連結</h2><p>本站可能包含其他網站的連結，這些網站的隱私權政策不在本政策範圍內。</p>
<h2>政策修訂</h2><p>本政策如有修訂，將公告於本頁面。如有疑問請<a href="contact.html">聯絡我們</a>。</p>''')
    page("404.html", f"找不到頁面｜{SITE_NAME}", "找不到頁面", f'<h1>找不到這個頁面</h1><p>回到<a href="./">首頁</a>看看所有工具。</p><div class="grid">{cards}</div>')
    urls = [""] + [f"{t.SLUG}.html" for t in tools] + ["about.html", "privacy.html", "contact.html"]
    (OUT/"sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
        "".join(f"<url><loc>{SITE_URL}/{u}</loc><lastmod>{UPDATED}</lastmod></url>\n" for u in urls) + "</urlset>\n")
    (OUT/"robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n")
    if ADSENSE_CLIENT:
        (OUT/"ads.txt").write_text(f"google.com, {ADSENSE_CLIENT.replace('ca-','')}, DIRECT, f08c47fec0942fa0\n")
    print(f"built {len(tools)} tools -> {OUT}")
build()
