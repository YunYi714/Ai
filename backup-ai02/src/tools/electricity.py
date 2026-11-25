SLUG="rent-electricity"; ORDER=1; NAV="電費檢查"
TITLE="租屋電費檢查計算機：房東一度電收太多了嗎？"
SHORT="輸入電費單金額和度數，馬上知道房東每度最多能收多少、多收了多少。"
DESC="租屋電費計算機：依2024年7月15日上路的租屋電費新制，房東每度電費不得超過電費單「當期每度平均電價」。輸入電費單總金額與度數，檢查房東是否超收並算出每月多付多少。"
FORM='''
<p class=note>先跟房東要這一期的台電電費單（或請房東告訴你單上的數字）。</p>
<div class="row"><div><label for="bill">電費單「每期電費總金額」（元）</label><input id="bill" inputmode="decimal" value="4200"></div>
<div><label for="kwh">電費單「當期用電度數」（度）</label><input id="kwh" inputmode="decimal" value="1200"></div></div>
<div class="row"><div><label for="rate">房東跟你收每度幾元</label><input id="rate" inputmode="decimal" value="5"></div>
<div><label for="use">你的電表每月用電度數</label><input id="use" inputmode="decimal" value="150"></div></div>
<button onclick="calc()">檢查電費</button><div class="result" id="out"></div>'''
JS=r'''
function calc(){const b=num('bill'),k=num('kwh'),r=num('rate'),u=num('use');if(b<=0||k<=0){show('out','請輸入電費單上的金額與度數');return}
 const avg=b/k,over=r-avg,ok=over<=0.005;
 show('out',`<div>這一期每度平均電價（房東收費上限）</div><div class="big">${fmt(avg,2)} 元／度</div>
 <p>${ok?'✅ 房東收 '+fmt(r,2)+' 元，沒有超過上限。':`❌ 房東收 <b>${fmt(r,2)}</b> 元，每度多收 <b>${fmt(over,2)}</b> 元。你每月用 ${fmt(u)} 度，<b>每月多付約 NT$ ${fmt(over*u)}</b>，一年約 NT$ ${fmt(over*u*12)}。`}</p>
 <p class=note>上限 = 每期電費總金額 ÷ 當期用電度數。每一期的平均電價都不同（夏月通常較高），房東應依當期電費單計算。適用 2024/7/15 以後簽訂、或雙方同意改用新制的租約。</p>`)}'''
ARTICLE='''
<h2>租屋電費新制（2024 年 7 月 15 日起）</h2>
<ul><li>房間沒有獨立台電電表、<b>按度計費</b>：每度電費<b>不得超過電費單上的「當期每度平均電價」</b>。</li>
<li><b>不按度計費</b>（例如大家分攤）：收的電費總額不得超過電費單的「每期電費總金額」。</li>
<li>屋外公共設施的電費，如果沒有併入這張電費單，房東不能另外向你收。</li>
<li>電費資訊要透明：平均電價、用電度數、電費總額等，房東應提供，房客也可以向台電申辦線上查詢。</li>
<li>違規經限期改正仍不改，依《消費者保護法》可處 3 萬至 50 萬元罰鍰。</li></ul>
<h2>計算範例</h2><p>電費單總金額 4,200 元、用電 1,200 度，平均每度 3.5 元。房東如果每度收 5 元，你每月用 150 度，每月就多付 225 元，一年多付 2,700 元。</p>'''
FAQ=[("房東說一度 5 元是行情，合法嗎？","依新制，按度計費不得超過電費單的當期每度平均電價。實際上限要看每一期的電費單，用電量大的夏月可能較高，非夏月通常較低，可以用上方計算機檢查。"),
("我的租約是 2024 年 7 月以前簽的，也適用嗎？","新制不溯及既往，舊約原則上依原本約定。但雙方可以同意改用新制；續約或重新簽約時就會適用。"),
("房東不給我看電費單怎麼辦？","電費資訊應透明，你可以要求房東提供，或向當地縣市政府消保官、地政單位詢問、申訴。")]
