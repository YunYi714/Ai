SLUG="deposit-penalty"; ORDER=2; NAV="押金違約金"
TITLE="押金與提前解約違約金檢查"
SHORT="押金最多 2 個月租金、提前解約違約金最多 1 個月。輸入租金馬上檢查。"
DESC="押金違約金計算機：依租賃住宅市場發展及管理條例，住宅押金不得超過2個月租金；依住宅租賃定型化契約，提前終止違約金最高1個月租金。輸入月租、押金與違約金，檢查房東有沒有多收。"
FORM='''
<div class="row"><div><label for="rent">每月租金（元）</label><input id="rent" inputmode="decimal" value="8000"></div>
<div><label for="dep">房東收的押金（元）</label><input id="dep" inputmode="decimal" value="24000"></div></div>
<label for="pen">租約寫的提前解約違約金（元，沒寫填 0）</label><input id="pen" inputmode="decimal" value="16000">
<button onclick="calc()">檢查</button><div class="result" id="out"></div>'''
JS=r'''
function calc(){const r=num('rent'),d=num('dep'),p=num('pen');if(r<=0){show('out','請輸入月租');return}
 const dm=r*2,pm=r;let h='';
 h+=d>dm?`<p>❌ <b>押金超收 NT$ ${fmt(d-dm)}</b>：押金最多 2 個月租金（NT$ ${fmt(dm)}）。超過的部分約定無效，你可以要求退還或抵扣之後的房租。</p>`:`<p>✅ 押金 NT$ ${fmt(d)} 沒有超過上限 NT$ ${fmt(dm)}。</p>`;
 h+=p>pm?`<p>❌ <b>違約金超過上限 NT$ ${fmt(p-pm)}</b>：租約約定可以提前終止時，違約金最多 1 個月租金（NT$ ${fmt(pm)}）。</p>`:p>0?`<p>✅ 違約金 NT$ ${fmt(p)} 沒有超過 1 個月租金。</p>`:'';
 show('out',`<div class="big">${d>dm||p>pm?'⚠️ 發現問題':'✅ 沒有超收'}</div>${h}<p class=note>押金上限依《租賃住宅市場發展及管理條例》第7條；違約金上限依內政部住宅租賃定型化契約應記載事項。</p>`)}'''
ARTICLE='''
<h2>押金規定</h2><ul><li>住宅租賃押金<b>不得超過 2 個月租金</b>（租賃住宅市場發展及管理條例第7條、土地法第99條）。</li>
<li>超收的部分約定無效，房客可以主張用超收的押金抵扣房租。</li><li>租約結束、你返還房屋時，房東應返還押金，只能扣除你積欠的租金、費用或你造成的損害。</li></ul>
<h2>提前解約規定</h2><ul><li>租約有約定可以提前終止：要<b>至少提前 1 個月通知</b>；沒有提前通知就終止，違約金<b>最多 1 個月租金</b>。</li>
<li>租約沒有約定可以提前終止：原則上不能任意終止，但遇到法定情況（例如房東不修繕致無法居住）可以終止，請看<a href="early-termination.html">提前解約懶人包</a>。</li>
<li>提前終止時，房東已經預收的租金要退還。</li></ul>'''
FAQ=[("押金收 3 個月，我已經簽約了怎麼辦？","超過 2 個月的部分約定無效。可以用文字要求房東退還，或主張抵扣之後的房租；房東不處理可以向縣市消保官或地政單位申訴。"),
("提前一個月通知，還要付違約金嗎？","如果租約約定可以提前終止，而你已經提前 1 個月通知，依定型化契約規定不需要付違約金。")]
