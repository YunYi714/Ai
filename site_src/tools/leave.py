SLUG="leave-deduction"; ORDER=0.3; NAV="請假扣薪"
TITLE="請假扣薪計算機（事假、病假、生理假、全勤獎金）"
SHORT="請一天假會被扣多少？全勤獎金可以扣嗎？2026 病假新制一起算。"
DESC="請假扣薪計算機：輸入月薪、全勤獎金、假別與天數，依勞工請假規則與性別平等工作法計算事假、病假、生理假、家庭照顧假可扣的薪資與全勤獎金上限，含2026年病假新制。"
FORM='''
<div class="row"><div><label for="w">月薪（不含全勤獎金）</label><input id="w" inputmode="decimal" value="32000"></div>
<div><label for="b">全勤獎金（沒有填 0）</label><input id="b" inputmode="decimal" value="2000"></div></div>
<div class="row"><div><label for="t">假別</label><select id="t">
<option value="p">事假</option><option value="f">家庭照顧假</option><option value="s">普通傷病假（病假）</option><option value="m">生理假</option>
<option value="o">特休、婚假、喪假、公假、公傷病假</option><option value="l">遲到（分鐘）</option></select></div>
<div><label for="d" id="dl">請假天數</label><input id="d" inputmode="decimal" value="1"></div></div>
<div id="sbox"><label for="used">今年已請過的病假天數（不含這次）</label><input id="used" inputmode="decimal" value="0"></div>
<button onclick="calc()">計算</button><div class="result" id="out"></div>'''
JS=r'''
$('t').onchange=()=>{const t=$('t').value;$('dl').textContent=t=='l'?'遲到幾分鐘':'請假天數';$('d').value=t=='l'?10:1;$('sbox').style.display=t=='s'?'block':'none'};$('t').onchange();
function calc(){const w=num('w'),b=num('b'),t=$('t').value,d=num('d'),day=w/30,hr=w/240;let ded=0,bmax=0,notes=[];
 if(t=='p'){ded=day*d;bmax=b;notes.push('事假一年 14 天內不給工資。全勤獎金能否扣、扣多少，依公司規定（工作規則或契約），但不能超過上表上限。')}
 else if(t=='f'){ded=day*d;bmax=0;notes.push('家庭照顧假併入事假計算（一年 7 天），不給工資，但<b>不能扣全勤獎金</b>，也不能有其他不利處分（性別平等工作法第20、21條）。可以按小時請。')}
 else if(t=='s'){const u=num('used'),half=Math.max(0,Math.min(d,30-u)),none=d-half;ded=day*0.5*half+day*none;bmax=b*d/30;
  notes.push('一年病假 30 天內（未住院）工資折半發給，超過的部分公司可以不給。');notes.push('2026 年新制：全勤獎金只能<b>依病假天數比例扣</b>（全勤 ÷ 30 × 天數），不能整筆扣光。');
  if(u+d<=10)notes.push('今年病假合計未超過 10 天：公司<b>不得</b>因此給你不利處分（例如考績、調薪、排班）。')}
 else if(t=='m'){ded=day*0.5*d;bmax=0;notes.push('生理假每月可請 1 天，工資減半發給，<b>不能扣全勤獎金</b>，也不能影響考績（性別平等工作法第14、21條）。一年 3 天內不併入病假。')}
 else if(t=='o'){ded=0;bmax=0;notes.push('這些假別工資照給，也<b>不能扣全勤獎金</b>。')}
 else{ded=hr*d/60;bmax=b;notes.push('遲到只能依實際遲到時間按比例扣薪。遲到 5 分鐘扣 1 小時、扣「罰款」都違法（勞基法第22、26條）。全勤獎金依公司規定處理。')}
 show('out',`<div>公司最多可以扣的薪資</div><div class="big">NT$ ${fmt(Math.round(ded))}</div>
 <table><tr><td>日薪（月薪 ÷ 30）</td><td class=n>${fmt(day)}</td></tr><tr><td>全勤獎金最多可扣</td><td class=n>NT$ ${fmt(Math.round(bmax))}</td></tr></table>
 <ul>${notes.map(n=>'<li>'+n+'</li>').join('')}</ul><p class=note>如果公司扣得比這裡算出的更多，可能已經違法。</p>`)}'''
ARTICLE='''
<h2>各種假別的工資與全勤獎金</h2>
<table><tr><th>假別</th><th>天數</th><th>工資</th><th>可以扣全勤嗎？</th></tr>
<tr><td>事假</td><td>一年 14 天</td><td>不給</td><td>依公司規定</td></tr>
<tr><td>家庭照顧假</td><td>一年 7 天（併入事假）</td><td>不給</td><td><b>不可以</b></td></tr>
<tr><td>普通傷病假</td><td>未住院一年 30 天</td><td>半薪</td><td>只能依比例扣（2026 新制）</td></tr>
<tr><td>生理假</td><td>每月 1 天</td><td>半薪</td><td><b>不可以</b></td></tr>
<tr><td>特休、婚假、喪假、公假、公傷病假</td><td>依規定</td><td>全薪</td><td><b>不可以</b></td></tr></table>
<h2>2026 年病假新制重點</h2><ul><li>一年病假 10 天內，公司不得因此在考績、調薪、排班等方面給你不利對待。</li><li>全勤獎金只能按病假天數比例扣。例如全勤 3,000 元、請 1 天病假，最多扣 100 元。</li><li>為了照顧家人請的事假，可以按小時請。</li></ul>'''
FAQ=[("請病假要附診斷證明嗎？","公司可以依工作規則要求提供證明，但不能刁難。一般短天數病假常見做法是事後補附就診證明。"),
("遲到 3 分鐘被扣 100 元合法嗎？","如果超過依時薪比例計算的金額，就是違法的「罰款」。用月薪 ÷ 240 算出時薪，再乘以遲到時間就是上限。")]
