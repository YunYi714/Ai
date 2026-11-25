SLUG="holiday-pay"; ORDER=0.2; NAV="國定假日"
TITLE="2027 國定假日一覽與出勤工資計算機"
SHORT="勞工一年 16 天國定假日，上班要給雙倍。算算你該拿多少。"
DESC="2027年勞工國定假日共16天（含小年夜、教師節、光復節、行憲紀念日）。輸入月薪或時薪與出勤天數，計算國定假日出勤應加倍發給的工資，工讀生、兼職也適用。"
FORM='''
<div class="row"><div><label for="type">計薪方式</label><select id="type"><option value="h">時薪（工讀、兼職）</option><option value="m">月薪</option></select></div>
<div><label for="pay" id="payLabel">時薪</label><input id="pay" inputmode="decimal" value="205"></div></div>
<div class="row"><div><label for="d">國定假日出勤幾天</label><input id="d" inputmode="numeric" value="1"></div>
<div><label for="h">每天工作幾小時</label><input id="h" inputmode="decimal" value="8"></div></div>
<button onclick="calc()">計算</button><div class="result" id="out"></div>'''
JS=r'''
$('type').onchange=()=>{const m=$('type').value=='m';$('payLabel').textContent=m?'月薪':'時薪';$('pay').value=m?32000:205};
function calc(){const m=$('type').value=='m',p=num('pay'),d=Math.round(num('d'));let h=Math.min(num('h'),12);if(p<=0||d<=0||h<=0){show('out','請輸入正確數字');return}
 const hr=m?p/240:p,base=m?hr*8:hr*Math.min(h,8),ot=hr*(Math.max(0,Math.min(h,10)-8)*4/3+Math.max(0,h-10)*5/3),per=base+ot;
 show('out',`<div>除了原本的工資，每出勤 1 天應「另外加發」</div><div class="big">NT$ ${fmt(Math.round(per))}</div>
 <p>${d} 天合計加發 <b>NT$ ${fmt(Math.round(per*d))}</b>。</p>
 <table><tr><td>${m?'加倍發給 1 日工資（月薪 ÷ 30）':'8 小時內加倍（時薪 × 工時）'}</td><td class=n>${fmt(base)}</td></tr>${ot?`<tr><td>超過 8 小時的加班費</td><td class=n>${fmt(ot)}</td></tr>`:''}</table>
 <p class=note>${m?'月薪制：國定假日的工資已包含在月薪中，出勤時要再加發一日工資。':'時薪制：國定假日如果是你原本排定的上班日，就算放假也要照付工資；當天叫你上班，要再加發一倍。'}</p>`)}
const H=[['2027-01-01','開國紀念日'],['2027-02-04','小年夜（除夕前一日）'],['2027-02-05','除夕'],['2027-02-06','春節（初一）'],['2027-02-07','春節（初二）'],['2027-02-08','春節（初三）'],['2027-02-28','和平紀念日'],['2027-04-04','兒童節'],['2027-04-05','民族掃墓節（清明）'],['2027-05-01','勞動節'],['2027-06-09','端午節'],['2027-09-15','中秋節'],['2027-09-28','教師節（孔子誕辰紀念日）'],['2027-10-10','國慶日'],['2027-10-25','臺灣光復暨金門古寧頭大捷紀念日'],['2027-12-25','行憲紀念日']];
$('hl').innerHTML='<tr><th>日期</th><th>星期</th><th>節日</th></tr>'+H.map(([d,n])=>{const t=new Date(d+'T00:00');return`<tr><td>${t.getMonth()+1}/${t.getDate()}</td><td>${'日一二三四五六'[t.getDay()]}</td><td>${n}</td></tr>`}).join('');'''
ARTICLE='''
<h2>2027 年勞工國定假日（16 天）</h2><table id="hl"></table>
<p class=note>依《紀念日及節日實施條例》（2025 年 5 月公布）與勞基法第37條。國定假日剛好遇到你的例假或休息日，公司要在其他工作日給你補假，日期由勞資雙方協商，不一定和公務員行事曆的補假相同。</p>
<h2>國定假日上班，工資怎麼算？</h2>
<ul><li><b>月薪制</b>：月薪已包含國定假日的工資。當天上班，公司要<b>再加發一日工資</b>（月薪 ÷ 30）。工作 8 小時以內都算一日。</li>
<li><b>時薪制（工讀、兼職）</b>：國定假日如果是你原本排班要上班的日子，放假也要照付；叫你上班就要<b>加倍</b>。</li>
<li>超過 8 小時的部分：第 9–10 小時 × 1又1/3、第 11–12 小時 × 1又2/3。</li></ul>
<p>國定假日可以經勞資雙方事先協商，和其他工作日對調。但沒有對調、當天又叫你上班，就一定要加倍。</p>'''
FAQ=[("餐飲、零售業「本來就沒有國定假日」嗎？","不對。勞基法適用所有行業，排班制也一樣有 16 天國定假日。公司可以協商把國定假日移到其他日子休，但不能直接不算。"),
("工讀生國定假日有雙倍嗎？","有。部分工時勞工同樣適用國定假日規定。"),
("公司說國定假日上班「給補休就好」可以嗎？","國定假日出勤依法應加倍發給工資。如果想用其他日子休假取代，必須在事前經你同意、把國定假日與工作日對調，不能事後片面用補休取代加倍工資。")]
