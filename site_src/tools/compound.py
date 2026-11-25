SLUG="compound-interest"; ORDER=8
TITLE="複利計算機（定期定額存錢試算）"
SHORT="每月存一點，幾年後會變多少？用複利算給你看。"
DESC="複利計算機：輸入本金、每月投入金額、年報酬率與年數，試算定期定額存錢或投資的未來總額、總投入與複利收益，並列出逐年成長表。"
FORM='''
<div class="row"><div><label for="P">一開始的本金</label><input id="P" inputmode="decimal" value="10000"></div>
<div><label for="A">每月投入</label><input id="A" inputmode="decimal" value="3000"></div></div>
<div class="row"><div><label for="r">預估年報酬率（%）</label><input id="r" inputmode="decimal" value="5"></div>
<div><label for="y">年數</label><input id="y" inputmode="numeric" value="20"></div></div>
<button onclick="calc()">計算</button><div class="result" id="out"></div>'''
JS=r'''
function calc(){const P=num('P'),A=num('A'),r=num('r')/100/12,Y=Math.round(num('y'));if(Y<=0){show('out','請輸入年數');return}
 let v=P,inv=P,rows='';for(let m=1;m<=Y*12;m++){v=v*(1+r)+A;inv+=A;if(m%12==0)rows+=`<tr><td>${m/12}</td><td class=n>${fmt(inv)}</td><td class=n>${fmt(v)}</td><td class=n>${fmt(v-inv)}</td></tr>`}
 show('out',`<div>${Y} 年後約有</div><div class="big">NT$ ${fmt(v)}</div><table><tr><td>總投入</td><td class=n>NT$ ${fmt(inv)}</td></tr><tr><td>複利收益</td><td class=n>NT$ ${fmt(v-inv)}</td></tr></table>
 <details><summary>逐年明細</summary><div class=scroll><table><tr><th>年</th><th>累積投入</th><th>總金額</th><th>收益</th></tr>${rows}</table></div></details>
 <p class=note>以每月複利、月底投入估算。投資報酬率不保證，過去績效不代表未來。</p>`)}'''
ARTICLE='''
<h2>複利是什麼？</h2><p>複利就是「利息也會再生利息」。時間越長，效果越明顯，所以越早開始存錢，差距越大。</p>
<h2>72 法則</h2><p>用 72 除以年報酬率，可以粗估資產翻倍需要幾年。例如年報酬 6%，大約 72 ÷ 6 = 12 年翻倍。</p>
<h2>報酬率要填多少？</h2><ul><li>銀行定存：約 1–2%</li><li>債券型投資：約 2–5%</li><li>全球股票指數長期歷史平均：約 6–8%（波動大、不保證）</li></ul>'''
FAQ=[("每月存 5,000 元，20 年後有多少？","以年報酬 5% 估算，20 年共投入 120 萬，最後約 205 萬元。可以直接用上方計算機調整數字試算。")]
