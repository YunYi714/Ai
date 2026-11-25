SLUG="rent-tax-deduction"; ORDER=3; NAV="租金報稅"
TITLE="租金支出特別扣除額試算：租屋報稅可以省多少？"
SHORT="租金每戶最高可扣 18 萬，不用跟標準扣除額二選一。算算你能退多少稅。"
DESC="租金支出特別扣除額試算：租屋族報稅每戶最高可扣除18萬元，且可與標準扣除額同時使用。輸入全年租金、租金補貼與適用稅率，試算可以少繳多少所得稅，附申報資格與必備文件。"
FORM='''
<div class="row"><div><label for="rent">全年實際支付租金（元）</label><input id="rent" inputmode="decimal" value="120000"></div>
<div><label for="sub">全年領到的政府租金補貼（沒有填 0）</label><input id="sub" inputmode="decimal" value="0"></div></div>
<label for="rate">你的綜合所得稅適用稅率</label><select id="rate"><option value="0.05">5%</option><option value="0.12">12%</option><option value="0">20% 以上（不適用）</option><option value="-1">不知道</option></select>
<button onclick="calc()">試算</button><div class="result" id="out"></div>'''
JS=r'''
function calc(){const r=num('rent'),s=num('sub'),t=parseFloat($('rate').value);const ded=Math.min(Math.max(r-s,0),180000);
 if(t==0){show('out','<div class="big">不適用</div><p>適用稅率 20% 以上（或股利選擇 28% 分開計稅、基本所得額超過 750 萬）的申報戶，不能申報租金支出特別扣除額。</p>');return}
 const rows=(t<0?[0.05,0.12]:[t]).map(x=>`<tr><td>稅率 ${x*100}%</td><td class=n>NT$ ${fmt(ded*x)}</td></tr>`).join('');
 show('out',`<div>可以申報的扣除額</div><div class="big">NT$ ${fmt(ded)}</div><p>預估可以少繳的稅：</p><table>${rows}</table>
 <p class=note>扣除額 = 全年租金 − 政府租金補貼，每一申報戶最高 18 萬元。實際節稅金額依你的所得與其他扣除額而定，以財政部報稅系統試算為準。</p>`)}'''
ARTICLE='''
<h2>租金支出特別扣除額重點</h2><ul><li>每一申報戶<b>最高 18 萬元</b>。</li><li>是「特別扣除額」，<b>不管你選標準扣除額或列舉扣除額都可以額外申報</b>。</li>
<li>可扣除金額 = 全年支付的租金 − 政府租金補貼。</li><li>條件：本人、配偶或受扶養直系親屬在國內租屋<b>自住</b>，不能是營業或執行業務使用。</li>
<li>申報戶名下有房屋原則上不能申報，但有例外，例如因工作、就學、就醫需要在外地租屋等（詳細請看財政部說明）。</li>
<li>排除：適用稅率 20% 以上、股利選擇 28% 分開計稅，或基本所得額超過 750 萬元的申報戶。</li></ul>
<h2>要準備什麼？</h2><ul><li>租賃契約書</li><li>付款證明（轉帳紀錄、收據等）</li><li>依國稅局要求可能需要的自住切結等文件</li></ul>
<h2>房東可以禁止我報稅嗎？</h2><p>不行。內政部住宅租賃定型化契約<b>不得約定房客不得申報租賃費用支出</b>，這種條款無效。詳細請看<a href="tax-household.html">報稅與遷戶籍懶人包</a>。</p>'''
FAQ=[("學生租屋可以申報嗎？","如果你是受扶養的子女，由扶養你的父母申報戶申報，只要符合自住、未超過排富門檻等條件就可以。"),
("我跟室友合租，怎麼報？","各自申報自己實際支付的租金部分，並準備自己的付款證明。")]
