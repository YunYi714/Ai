SLUG="annual-leave"; ORDER=2
TITLE="特休天數計算機（勞基法第38條）"
SHORT="輸入到職日，算出你今年有幾天特休、下一次增加是什麼時候。"
DESC="特休計算機：輸入到職日期，依勞基法第38條自動計算年資與特別休假天數（週年制），並列出未來各年度的特休天數表。"
FORM='''
<div class="row"><div><label for="start">到職日</label><input id="start" type="date" value="2024-03-01"></div>
<div><label for="end">計算基準日</label><input id="end" type="date" data-today></div></div>
<button onclick="calc()">計算特休天數</button><div class="result" id="out"></div>'''
JS=r'''
function days(y,m){const t=y+m/12;if(t<0.5)return 0;if(t<1)return 3;if(t<2)return 7;if(t<3)return 10;if(t<5)return 14;if(t<10)return 15;return Math.min(30,15+Math.floor(t)-9)}
function addM(d,m){const r=new Date(d);r.setMonth(r.getMonth()+m);return r}
function ds(d){return d.getFullYear()+'/'+(d.getMonth()+1)+'/'+d.getDate()}
function calc(){const s=new Date($('start').value),e=new Date($('end').value);if(isNaN(s)||isNaN(e)||e<s){show('out','請確認日期是否正確');return}
 const r=diffYMD(s,e),now=days(r.y,r.m);
 const marks=[[6,'滿 6 個月'],[12,'滿 1 年'],[24,'滿 2 年'],[36,'滿 3 年'],[60,'滿 5 年'],[120,'滿 10 年']];for(let y=11;y<=24;y++)marks.push([y*12,'滿 '+y+' 年']);
 let tb='',next='';for(const[m,l]of marks){const d=addM(s,m),dd=days(Math.floor(m/12),m%12),past=d<=e;
  tb+=`<tr${past?' style="color:#999"':''}><td>${l}</td><td>${ds(d)}</td><td class=n>${dd} 天</td></tr>`;if(!past&&!next)next=`下一次：<b>${ds(d)}</b>（${l}）起，特休 <b>${dd}</b> 天`}
 show('out',`<div>目前年資：${r.y} 年 ${r.m} 個月 ${r.d} 天</div><div>目前這一個年度的特休</div><div class="big">${now} 天</div><p>${next}</p>
 <div class=scroll><table><tr><th>年資</th><th>日期</th><th>該年度特休</th></tr>${tb}</table></div>
 <p class=note>以「週年制」（依到職日起算）計算。公司若採曆年制、會計年度制，可能依比例計算，但總天數不得少於週年制。</p>`)}'''
ARTICLE='''
<h2>特休天數表（勞基法第38條）</h2>
<table><tr><th>年資</th><th>特休天數</th></tr><tr><td>6 個月以上、未滿 1 年</td><td>3 天</td></tr><tr><td>1 年以上、未滿 2 年</td><td>7 天</td></tr>
<tr><td>2 年以上、未滿 3 年</td><td>10 天</td></tr><tr><td>3 年以上、未滿 5 年</td><td>每年 14 天</td></tr><tr><td>5 年以上、未滿 10 年</td><td>每年 15 天</td></tr>
<tr><td>10 年以上</td><td>每 1 年加 1 天，最多 30 天</td></tr></table>
<p>例如 2024 年 3 月 1 日到職：2024/9/1 滿半年有 3 天、2025/3/1 滿一年有 7 天、2026/3/1 滿兩年有 10 天。</p>'''
FAQ=[("特休沒休完怎麼辦？","年度終結或契約終止時未休完的特休，雇主應發給工資。勞資雙方也可以協商遞延到下一年度，但遞延後仍未休完的，應發給工資。"),
("特休日期誰決定？","依法由勞工排定，雇主若有急迫需求或勞工因個人因素，雙方可以協商調整。"),
("兼職、工讀生有特休嗎？","有。部分工時勞工也適用特休規定，依其工作時數與全時勞工的比例計算時數。")]
