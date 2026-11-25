SLUG="roommate-split"; ORDER=4; NAV="室友分攤"
TITLE="室友房租水電分攤計算機（依房間坪數）"
SHORT="房間大小不同怎麼分房租？輸入坪數，自動算出公平的分攤金額。"
DESC="室友分租計算機：合租時房間大小不同，依各房間坪數與公共空間比例分攤房租，水電網路平均分攤，自動算出每個人要付多少，避免室友吵架。"
FORM='''
<div class="row"><div><label for="rent">每月總房租</label><input id="rent" inputmode="decimal" value="30000"></div>
<div><label for="util">每月水電網路瓦斯等（平均分）</label><input id="util" inputmode="decimal" value="2400"></div></div>
<label for="common">公共空間（客廳、廚房）佔房租的比例 %（平均分攤）</label><input id="common" inputmode="decimal" value="30">
<label for="rooms">每個人的房間坪數（用逗號分開，例如 4,3,2.5）</label><input id="rooms" value="4,3,2.5">
<label for="names">名字（可選，用逗號分開）</label><input id="names" value="小明,小華,小美">
<button onclick="calc()">計算分攤</button><div class="result" id="out"></div>'''
JS=r'''
function calc(){const R=num('rent'),U=num('util'),c=Math.min(Math.max(num('common'),0),100)/100;
 const rooms=$('rooms').value.split(/[,，、\s]+/).map(Number).filter(x=>x>0);if(!rooms.length){show('out','請輸入房間坪數');return}
 const names=$('names').value.split(/[,，、]+/).map(s=>s.trim());const n=rooms.length,tot=rooms.reduce((a,b)=>a+b,0);
 let rows='',sum=0;rooms.forEach((a,i)=>{const v=R*c/n+R*(1-c)*a/tot+U/n;sum+=v;rows+=`<tr><td>${names[i]||'室友'+(i+1)}</td><td class=n>${a}</td><td class=n>${fmt(R*c/n+R*(1-c)*a/tot)}</td><td class=n>${fmt(U/n)}</td><td class=n><b>${fmt(v)}</b></td></tr>`});
 show('out',`<div class=scroll><table><tr><th>人</th><th>坪數</th><th>房租</th><th>水電等</th><th>每月合計</th></tr>${rows}<tr><td colspan=4>總計</td><td class=n>${fmt(sum)}</td></tr></table></div>
 <p class=note>房租 = 公共空間部分平均分 + 其餘依房間坪數比例分。有獨立衛浴、陽台的房間，可以把坪數加一點反映價值。</p>`)}'''
ARTICLE='''<h2>怎麼分才公平？</h2><p>常見的做法是：客廳、廚房等公共空間大家平均分攤，房間的部分依坪數比例分攤。公共空間的比例通常設 20%–40%。</p>
<p>有獨立衛浴、對外窗、陽台的房間比較有價值，可以把坪數「加權」，例如獨立衛浴加 1 坪。</p>
<h2>合租提醒</h2><ul><li>最好由每個人都和房東簽約，或至少讓房東知道誰住在這裡，避免二房東問題。</li><li>電費如果是房東按度收，記得用<a href="rent-electricity.html">電費檢查計算機</a>看有沒有超收。</li></ul>'''
FAQ=[("室友不付錢怎麼辦？","如果租約只有一個人的名字，對房東負責的是簽約人。合租前最好簽一份室友協議，寫清楚分攤方式與搬走的規則。")]
