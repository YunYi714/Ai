SLUG="loan"; ORDER=7
TITLE="房貸／信貸每月還款計算機（含寬限期）"
SHORT="本息平均攤還、本金平均攤還、寬限期，一次算出月付金與總利息。"
DESC="房貸計算機：輸入貸款金額、年利率、年限與寬限期，計算本息平均攤還或本金平均攤還的每月還款金額、總利息，並列出每年還款明細。"
FORM='''
<div class="row"><div><label for="P">貸款金額（萬元）</label><input id="P" inputmode="decimal" value="800"></div>
<div><label for="rate">年利率（%）</label><input id="rate" inputmode="decimal" value="2.185"></div></div>
<div class="row"><div><label for="yrs">貸款年限（年）</label><input id="yrs" inputmode="numeric" value="30"></div>
<div><label for="g">寬限期（年，只繳利息）</label><input id="g" inputmode="numeric" value="0"></div></div>
<label for="mode">還款方式</label><select id="mode"><option value="a">本息平均攤還（每月金額固定）</option><option value="p">本金平均攤還（前高後低）</option></select>
<button onclick="calc()">計算</button><div class="result" id="out"></div>'''
JS=r'''
function calc(){const P=num('P')*10000,r=num('rate')/100/12,N=Math.round(num('yrs')*12),G=Math.min(Math.round(num('g')*12),N-1),mode=$('mode').value;
 if(P<=0||N<=0){show('out','請輸入正確數字');return}
 let bal=P,ti=0,rows='',yi=0,yp=0,first=0,afterG=0,last=0;const n=N-G,M=r==0?P/n:P*r/(1-Math.pow(1+r,-n));
 for(let k=1;k<=N;k++){const i=bal*r;let pr=0;if(k>G)pr=mode=='a'?M-i:P/n;if(k==N)pr=bal;const pay=i+pr;
  if(k==1)first=pay;if(k==G+1)afterG=pay;last=pay;bal-=pr;ti+=i;yi+=i;yp+=pr;
  if(k%12==0||k==N){rows+=`<tr><td>第 ${Math.ceil(k/12)} 年</td><td class=n>${fmt(yp)}</td><td class=n>${fmt(yi)}</td><td class=n>${fmt(Math.max(bal,0))}</td></tr>`;yi=0;yp=0}}
 show('out',`${G?`<div>寬限期每月（只繳利息）：<b>NT$ ${fmt(first)}</b></div><div>寬限期後每月${mode=='p'?'（第一期）':''}</div>`:`<div>每月還款${mode=='p'?'（第一期）':''}</div>`}
 <div class="big">NT$ ${fmt(afterG)}</div>${mode=='p'?`<div>最後一期：NT$ ${fmt(last)}</div>`:''}
 <table><tr><td>總利息</td><td class=n>NT$ ${fmt(ti)}</td></tr><tr><td>本利和</td><td class=n>NT$ ${fmt(P+ti)}</td></tr></table>
 <details><summary>每年還款明細</summary><div class=scroll><table><tr><th>年度</th><th>償還本金</th><th>利息</th><th>年底剩餘本金</th></tr>${rows}</table></div></details>
 <p class=note>以固定利率估算。實際利率會隨央行調息與銀行方案變動。</p>`)}'''
ARTICLE='''
<h2>本息平均攤還 vs 本金平均攤還</h2>
<p><b>本息平均攤還</b>：每月還款金額固定，前期繳的大多是利息，比較好規劃預算，是最常見的方式。</p>
<p><b>本金平均攤還</b>：每月償還相同本金，利息隨本金減少而降低，所以每月金額前高後低，<b>總利息比較少</b>，但前期壓力較大。</p>
<h2>寬限期是什麼？</h2>
<p>寬限期內只繳利息、不還本金，前幾年壓力較小。但寬限期結束後，本金要在剩下的年限內還完，每月金額會明顯變高，<b>總利息也會增加</b>。</p>
<h2>計算公式</h2><p>本息平均攤還每月金額 = 貸款本金 × 月利率 ÷ (1 − (1 + 月利率)<sup>−期數</sup>)</p>'''
FAQ=[("新青安貸款可以用這個算嗎？","可以。輸入核貸金額、目前適用的利率、40 年（或實際年限）與寬限期（最長 5 年）即可估算。"),
("提前還款可以省多少利息？","提前還一筆本金後，把剩餘本金和剩餘年限重新輸入，就可以和原本的總利息比較。")]
