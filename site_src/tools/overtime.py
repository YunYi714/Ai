SLUG="overtime"; ORDER=1
TITLE="加班費計算機（平日、休息日、國定假日）"
SHORT="輸入月薪與加班時數，依勞基法第24、39條自動算出加班費。"
DESC="免費加班費計算機：輸入月薪或時薪、加班時數，依勞基法自動計算平日加班、休息日加班、國定假日出勤的加班費，附倍率說明與常見問題。"
FORM='''
<div class="row"><div><label for="type">計薪方式</label><select id="type"><option value="m">月薪</option><option value="h">時薪</option></select></div>
<div><label for="pay" id="payLabel">月薪（含經常性津貼）</label><input id="pay" inputmode="decimal" value="32000"></div></div>
<div class="row"><div><label for="kind">加班日類型</label><select id="kind">
<option value="w">平日（工作日）延長工時</option><option value="r">休息日出勤</option><option value="h">國定假日／特休日出勤</option></select></div>
<div><label for="hrs" id="hrsLabel">加班時數（小時）</label><input id="hrs" inputmode="decimal" value="2"></div></div>
<button onclick="calc()">計算加班費</button><div class="result" id="out"></div>'''
JS=r'''
$('type').onchange=()=>{$('payLabel').textContent=$('type').value=='m'?'月薪（含經常性津貼）':'時薪';$('pay').value=$('type').value=='m'?32000:205};
$('kind').onchange=()=>{$('hrsLabel').textContent=$('kind').value=='w'?'加班時數（小時，正常工時以外）':'當天實際出勤時數（小時）'};
function calc(){const t=$('type').value,k=$('kind').value,p=num('pay');let h=num('hrs');
 if(p<=0||h<=0){show('out','請輸入大於 0 的薪資與時數');return}
 const hr=t=='m'?p/240:p;let rows=[],tot=0,warn='';
 const seg=(name,hours,rate,label)=>{if(hours<=0)return;const v=hr*hours*rate;tot+=v;rows.push(`<tr><td>${name}</td><td class=n>${fmt(hours,1)}</td><td>${label}</td><td class=n>${fmt(v)}</td></tr>`)};
 if(k=='w'){if(h>4){warn='平日延長工時加上正常工時，一天不得超過 12 小時（延長最多 4 小時）。以下以 4 小時計。';h=4}
  seg('前 2 小時',Math.min(h,2),4/3,'× 1又1/3');seg('第 3–4 小時',Math.max(0,h-2),5/3,'× 1又2/3')}
 else if(k=='r'){if(h>12){warn='休息日出勤一天最多 12 小時，以下以 12 小時計。';h=12}
  seg('前 2 小時',Math.min(h,2),4/3,'× 1又1/3');seg('第 3–8 小時',Math.max(0,Math.min(h,8)-2),5/3,'× 1又2/3');seg('第 9–12 小時',Math.max(0,h-8),8/3,'× 2又2/3')}
 else{if(h>12){warn='一天最多 12 小時，以下以 12 小時計。';h=12}
  if(t=='m'){const v=hr*8;tot+=v;rows.push(`<tr><td>8 小時內（加倍發給一日工資）</td><td class=n>${fmt(Math.min(h,8),1)}</td><td>加發 1 日（8 小時）</td><td class=n>${fmt(v)}</td></tr>`)}
  else{seg('8 小時內（加倍發給）',Math.min(h,8),1,'× 1（另加）')}
  seg('第 9–10 小時',Math.max(0,Math.min(h,10)-8),4/3,'× 1又1/3');seg('第 11–12 小時',Math.max(0,h-10),5/3,'× 1又2/3')}
 show('out',`${warn?'<p class=note>⚠️ '+warn+'</p>':''}<div>換算時薪：<b>${fmt(hr,2)}</b> 元${t=='m'?'（月薪 ÷ 240）':''}</div>
 <div>應領加班費約</div><div class="big">NT$ ${fmt(Math.round(tot))}</div>
 <table><tr><th>區段</th><th>時數</th><th>倍率</th><th>金額</th></tr>${rows.join('')}</table>
 <p class=note>${k=='h'?'國定假日出勤的「加倍發給」是在原本照給的當日工資之外，額外再發給的金額。':'金額為原本薪資以外額外加給的加班費。'}實際金額以公司計算與勞工主管機關解釋為準。</p>`)}'''
ARTICLE='''
<h2>加班費怎麼算？</h2>
<p>依《勞動基準法》，月薪制勞工的時薪通常以「<b>月薪 ÷ 30 ÷ 8 = 月薪 ÷ 240</b>」換算，月薪應包含經常性給與（例如固定的職務加給、全勤獎金等）。</p>
<table><tr><th>情境</th><th>時段</th><th>加給倍率（時薪 ×）</th></tr>
<tr><td rowspan=2>平日延長工時（第24條第1項）</td><td>前 2 小時</td><td>1又1/3</td></tr><tr><td>第 3–4 小時</td><td>1又2/3</td></tr>
<tr><td rowspan=3>休息日出勤（第24條第2項）</td><td>前 2 小時</td><td>1又1/3</td></tr><tr><td>第 3–8 小時</td><td>1又2/3</td></tr><tr><td>第 9–12 小時</td><td>2又2/3</td></tr>
<tr><td rowspan=3>國定假日／特休日出勤（第39條）</td><td>8 小時內</td><td>加倍發給一日工資</td></tr><tr><td>第 9–10 小時</td><td>1又1/3</td></tr><tr><td>第 11–12 小時</td><td>1又2/3</td></tr></table>
<h2>計算範例</h2>
<p>月薪 36,000 元，時薪 = 36,000 ÷ 240 = 150 元。平日加班 3 小時：前 2 小時 150 × 4/3 × 2 = 400 元，第 3 小時 150 × 5/3 × 1 = 250 元，合計 <b>650 元</b>。</p>
<p>同樣月薪，休息日出勤 8 小時：前 2 小時 400 元 + 第 3–8 小時 150 × 5/3 × 6 = 1,500 元，合計 <b>1,900 元</b>。</p>'''
FAQ=[("休息日加班還是「做 1 給 4」嗎？","不是。2018 年修法後，休息日出勤改為依實際工作時數計算加班費，不再有做 1 小時給 4 小時的規定。"),
("月薪要不要含津貼、獎金？","計算時薪的基礎應包含「經常性給與」，例如固定的職務加給、伙食津貼、全勤獎金等；年終獎金、三節獎金等非經常性給與則不計入。"),
("公司可以用補休代替加班費嗎？","依勞基法第32條之1，需由勞工自行選擇補休並經雇主同意才可以；補休期限屆滿或契約終止時未休完的時數，雇主應依原本的加班費標準發給工資。"),
("例假日（每週一天的例假）可以加班嗎？","原則上不行。只有在天災、事變或突發事件時才可以要求例假日出勤，且工資應加倍發給並給予補假休息。")]
