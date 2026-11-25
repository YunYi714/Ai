SLUG="notice-period"; ORDER=4; NAV="預告期"
TITLE="資遣預告期間與預告工資計算機"
SHORT="被資遣要提前幾天通知？沒預告可以拿多少預告工資？"
DESC="預告期間計算機：依勞基法第16條，輸入到職日與月薪，自動計算雇主資遣時應提前預告的天數、謀職假時數與未預告時應給付的預告工資。"
FORM='''
<div class="row"><div><label for="start">到職日</label><input id="start" type="date" value="2023-05-01"></div>
<div><label for="end">資遣通知日</label><input id="end" type="date" data-today></div></div>
<label for="wage">月薪</label><input id="wage" inputmode="decimal" value="36000">
<button onclick="calc()">計算</button><div class="result" id="out"></div>'''
JS=r'''
function calc(){const s=new Date($('start').value),e=new Date($('end').value),w=num('wage');if(isNaN(s)||isNaN(e)||e<s){show('out','請確認日期');return}
 const r=diffYMD(s,e),t=r.y+r.m/12;let d=0;if(t>=3)d=30;else if(t>=1)d=20;else if(t>=0.25)d=10;
 const pay=Math.round(w/30*d);
 show('out',`<div>年資：${r.y} 年 ${r.m} 個月 ${r.d} 天</div><div>雇主應提前預告</div><div class="big">${d} 天</div>
 ${d?`<p>若雇主沒有預告就直接資遣，應給付預告期間工資約 <b>NT$ ${fmt(pay)}</b>（日薪 ${fmt(w/30)} × ${d} 天）。</p><p>預告期間內，你每週可請最多 2 天「謀職假」，工資照給。</p>`:'<p>年資未滿 3 個月，法律未規定預告期間。</p>'}
 <p class=note>預告工資與資遣費是分開計算的兩筆錢。</p>`)}'''
ARTICLE='''
<h2>預告期間規定（勞基法第16條）</h2>
<table><tr><th>年資</th><th>預告期間</th></tr><tr><td>3 個月以上、未滿 1 年</td><td>10 日前預告</td></tr><tr><td>1 年以上、未滿 3 年</td><td>20 日前預告</td></tr><tr><td>3 年以上</td><td>30 日前預告</td></tr></table>
<p>雇主未依規定預告就終止契約，應給付預告期間的工資。勞工在接到預告後，為了另謀工作可以請謀職假，每星期不得超過 2 日，工資照給。</p>'''
FAQ=[("自己要離職也要預告嗎？","依勞基法第15條，勞工自請離職也應準用同樣的預告期間（定期契約另有規定）。"),
("預告工資要不要扣稅？","預告工資屬於薪資所得，依一般薪資所得規定處理。")]
