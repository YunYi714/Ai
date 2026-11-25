SLUG="severance"; ORDER=3
TITLE="資遣費計算機（勞退新制／舊制）"
SHORT="輸入到職日、離職日與平均工資，算出資遣費。"
DESC="資遣費計算機：輸入到職日、離職日與平均月薪，依勞工退休金條例（新制）或勞基法第17條（舊制）自動計算資遣費與年資，含計算範例。"
FORM='''
<div class="row"><div><label for="start">到職日</label><input id="start" type="date" value="2021-06-01"></div>
<div><label for="end">最後工作日</label><input id="end" type="date" data-today></div></div>
<div class="row"><div><label for="wage">平均月工資（最近 6 個月平均）</label><input id="wage" inputmode="decimal" value="36000"></div>
<div><label for="sys">退休金制度</label><select id="sys"><option value="new">勞退新制（2005/7/1 以後到職者）</option><option value="old">勞基法舊制</option></select></div></div>
<button onclick="calc()">計算資遣費</button><div class="result" id="out"></div>'''
JS=r'''
function calc(){const s=new Date($('start').value),e=new Date($('end').value),w=num('wage');if(isNaN(s)||isNaN(e)||e<s||w<=0){show('out','請確認日期與工資');return}
 e.setDate(e.getDate()+1);const r=diffYMD(s,e);let base,txt;
 if($('sys').value=='new'){base=Math.min(6,(r.y+r.m/12+r.d/365)*0.5);txt=`(${r.y} + ${r.m}/12 + ${r.d}/365) × 0.5 = ${fmt(base,4)} 個月${base>=6?'（已達上限 6 個月）':''}`}
 else{const m=r.m+(r.d>0?1:0);base=r.y+m/12;txt=`${r.y} + ${m}/12 = ${fmt(base,4)} 個月（未滿 1 個月以 1 個月計）`}
 show('out',`<div>年資：${r.y} 年 ${r.m} 個月 ${r.d} 天</div><div>資遣費基數：${txt}</div><div>資遣費約</div><div class="big">NT$ ${fmt(Math.round(base*w))}</div>
 <p class=note>年資以到職日至最後工作日（含當日）計算。新舊制年資併存者，需分段計算後相加。實際金額以主管機關認定為準。</p>`)}'''
ARTICLE='''
<h2>資遣費怎麼算？</h2>
<p><b>勞退新制</b>（勞工退休金條例第12條）：每滿 1 年發給 <b>1/2 個月</b>平均工資，未滿 1 年依比例計算，<b>最高 6 個月</b>。</p>
<p><b>勞基法舊制</b>（第17條）：每滿 1 年發給 <b>1 個月</b>平均工資，剩餘月數按比例計算，未滿 1 個月以 1 個月計，無上限。</p>
<p><b>平均工資</b>：事由發生當日前 6 個月內所得工資總額 ÷ 該期間總日數，再 × 30。一般可用最近 6 個月的平均月薪估算。</p>
<h2>計算範例</h2>
<p>新制、年資 3 年 4 個月 15 天、平均工資 40,000 元：(3 + 4/12 + 15/365) × 0.5 ≈ 1.6872 個月，資遣費約 <b>67,489 元</b>。</p>'''
FAQ=[("資遣費什麼時候要發？","依法應於終止勞動契約後 30 日內發給。"),
("自己離職有資遣費嗎？","一般自請離職沒有。但若是因雇主違法（例如積欠工資、未依法投保等），依勞基法第14條終止契約，可以請求資遣費。"),
("資遣費要繳稅嗎？","資遣費屬於退職所得，在一定額度內免稅，超過的部分依規定計算。詳細請參考財政部最新公告。")]
