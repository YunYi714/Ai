SLUG="installment-apr"; ORDER=6
TITLE="分期付款實際年利率計算機"
SHORT="「0 手續費」分期真的划算嗎？算出分期、貸款的真實年利率。"
DESC="分期付款利率計算機：輸入商品價格、期數、每期金額與手續費，算出分期付款或信貸的實際年利率（APR）與總利息，看清楚「低月付」背後的真實成本。"
FORM='''
<div class="row"><div><label for="price">商品價格／借款金額</label><input id="price" inputmode="decimal" value="30000"></div>
<div><label for="n">期數（月）</label><input id="n" inputmode="numeric" value="12"></div></div>
<div class="row"><div><label for="pmt">每期付款金額</label><input id="pmt" inputmode="decimal" value="2700"></div>
<div><label for="fee">一次性手續費／開辦費（沒有填 0）</label><input id="fee" inputmode="decimal" value="0"></div></div>
<button onclick="calc()">計算實際年利率</button><div class="result" id="out"></div>'''
JS=r'''
function pv(r,n,a){return r==0?a*n:a*(1-Math.pow(1+r,-n))/r}
function calc(){const P=num('price'),n=Math.round(num('n')),A=num('pmt'),f=num('fee'),net=P-f;
 if(P<=0||n<=0||A<=0||net<=0){show('out','請輸入正確數字');return}
 const total=A*n+0,int=total-net;let r;
 if(A*n<=net){r=0}else{let lo=0,hi=1;for(let i=0;i<200;i++){const m=(lo+hi)/2;pv(m,n,A)>net?lo=m:hi=m}r=(lo+hi)/2}
 const apr=r*12*100,ear=(Math.pow(1+r,12)-1)*100;
 show('out',`<div>實際年利率（APR）</div><div class="big">${fmt(apr,2)}%</div>
 <table><tr><td>總共要付</td><td class=n>NT$ ${fmt(A*n+f)}</td></tr><tr><td>比原價多付</td><td class=n>NT$ ${fmt(A*n+f-P)}</td></tr>
 <tr><td>月利率</td><td class=n>${fmt(r*100,3)}%</td></tr><tr><td>有效年利率（複利）</td><td class=n>${fmt(ear,2)}%</td></tr></table>
 <p class=note>${apr>16?'⚠️ 這個利率已經高於信用卡循環利息上限（15%）附近，非常不划算。':apr>8?'這個利率比一般個人信貸高，建議比較其他方案。':apr<0.01?'看起來是真的 0 利率。':'利率不算太高，但仍是借錢，請確認自己負擔得起。'}</p>`)}'''
ARTICLE='''
<h2>為什麼分期利率不能用「多付的錢 ÷ 本金」算？</h2>
<p>分期付款每個月都在還本金，你真正借用的錢越來越少。所以用「總利息 ÷ 本金 ÷ 年數」算出的「表面利率」，通常只有<b>實際利率的一半左右</b>。</p>
<p>例如 30,000 元的手機分 12 期、每期 2,700 元，總共多付 2,400 元。表面利率是 8%，但實際年利率約 <b>14.5%</b>。</p>
<p>本計算機用的是金融機構揭露「總費用年百分率」的同一種方法：找出讓「每期付款折現值 = 實際拿到的金額」的利率。</p>
<h2>使用小提醒</h2><ul><li>「每期金額」請填實際每月扣款金額（含利息）。</li><li>如果有開辦費、手續費，或是分期比現金價貴，都要算進去：價格填<b>現金價</b>，手續費填一次性的費用。</li></ul>'''
FAQ=[("0 利率分期真的沒有成本嗎？","如果分期總額等於現金價、而且沒有任何手續費，那就是真的 0 利率。但要注意，有些商家現金購買另有折扣，這時分期的「真實價格」其實比較貴。"),
("信用卡分期和信用貸款哪個划算？","把兩者的期數、每期金額和手續費輸入本計算機，比較實際年利率就知道了。")]
