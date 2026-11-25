const $=id=>document.getElementById(id);
const num=id=>{const v=parseFloat(String($(id).value).replace(/,/g,''));return isNaN(v)?0:v};
const fmt=(n,d=0)=>Number(n).toLocaleString('zh-TW',{minimumFractionDigits:d,maximumFractionDigits:d});
const show=(id,html)=>{const e=$(id);e.innerHTML=html;e.classList.add('show');e.scrollIntoView({behavior:'smooth',block:'nearest'})};
// 計算兩日期間的年、月、日（年資）
function diffYMD(a,b){let y=b.getFullYear()-a.getFullYear(),m=b.getMonth()-a.getMonth(),d=b.getDate()-a.getDate();
 if(d<0){m--;d+=new Date(b.getFullYear(),b.getMonth(),0).getDate()}if(m<0){y--;m+=12}return{y,m,d}}
function todayStr(){const t=new Date();return t.getFullYear()+'-'+String(t.getMonth()+1).padStart(2,'0')+'-'+String(t.getDate()).padStart(2,'0')}
document.querySelectorAll('input[data-today]').forEach(e=>{if(!e.value)e.value=todayStr()});
