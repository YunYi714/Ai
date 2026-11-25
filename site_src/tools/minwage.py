SLUG="minimum-wage"; ORDER=5
TITLE="2027 最低工資查詢與月薪時薪換算"
SHORT="2027 年月薪 30,900、時薪 205？檢查你的薪水有沒有低於最低工資。"
DESC="2027年（116年）最低工資月薪30,900元、時薪205元。輸入你的時薪與工時，換算月收入並檢查是否低於最低工資，附歷年最低工資表。"
FORM='''
<div class="row"><div><label for="yr">年度</label><select id="yr"><option value="2027">2027 年（116 年）</option><option value="2026">2026 年（115 年）</option></select></div>
<div><label for="type">計薪方式</label><select id="type"><option value="h">時薪</option><option value="m">月薪</option></select></div></div>
<div class="row"><div><label for="pay">你的薪資（元）</label><input id="pay" inputmode="decimal" value="200"></div>
<div><label for="hrs">每月工作時數（時薪制）</label><input id="hrs" inputmode="decimal" value="80"></div></div>
<button onclick="calc()">檢查</button><div class="result" id="out"></div>'''
JS=r'''
const MW={2027:{m:30900,h:205},2026:{m:29500,h:196}};
function calc(){const y=$('yr').value,t=$('type').value,p=num('pay'),h=num('hrs'),mw=MW[y];
 if(t=='h'){const ok=p>=mw.h;show('out',`<div>${y} 年最低時薪：<b>${mw.h}</b> 元</div><div class="big">${ok?'✅ 沒有低於最低工資':'❌ 低於最低工資'}</div>
  <p>你的時薪 ${fmt(p)} 元${ok?'':'，每小時少了 <b>'+fmt(mw.h-p)+'</b> 元'}。每月工作 ${fmt(h)} 小時，月收入約 <b>NT$ ${fmt(p*h)}</b>${ok?'':'，依法至少應有 NT$ '+fmt(mw.h*h)}。</p>`)}
 else{const ok=p>=mw.m;show('out',`<div>${y} 年最低月薪：<b>${fmt(mw.m)}</b> 元</div><div class="big">${ok?'✅ 沒有低於最低工資':'❌ 低於最低工資'}</div>
  <p>你的月薪 ${fmt(p)} 元${ok?'':'，每月少了 <b>'+fmt(mw.m-p)+'</b> 元'}。換算時薪約 ${fmt(p/240,1)} 元（月薪 ÷ 240）。</p>`)}}'''
ARTICLE='''
<h2>2027 年最低工資</h2>
<p>最低工資審議會於 2026 年 9 月 24 日決議，自 <b>2027 年 1 月 1 日</b>起：</p>
<ul><li>每月最低工資：29,500 元 → <b>30,900 元</b>（+1,400 元，調幅 4.75%）</li><li>每小時最低工資：196 元 → <b>205 元</b>（+9 元）</li></ul>
<p class=note>以行政院核定、勞動部正式公告為準。</p>
<h2>近年最低工資</h2>
<table><tr><th>實施日期</th><th>月薪</th><th>時薪</th></tr><tr><td>2027/1/1</td><td>30,900</td><td>205</td></tr><tr><td>2026/1/1</td><td>29,500</td><td>196</td></tr>
<tr><td>2025/1/1</td><td>28,590</td><td>190</td></tr><tr><td>2024/1/1</td><td>27,470</td><td>183</td></tr><tr><td>2023/1/1</td><td>26,400</td><td>176</td></tr></table>'''
FAQ=[("工讀生、兼職也適用最低工資嗎？","適用。時薪制的部分工時勞工，每小時工資不得低於最低時薪。"),
("月薪包含加班費嗎？","不包含。最低工資是指正常工作時間內的報酬，加班費、例假日與國定假日出勤加給的工資不能算進去。"),
("老闆給的薪水低於最低工資怎麼辦？","可以向工作所在地的縣市政府勞工局（處）申訴，或撥打 1955 勞工諮詢申訴專線。")]
