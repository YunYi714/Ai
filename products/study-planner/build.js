const {chromium}=require('playwright');const path=require('path');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
await p.goto('file://'+path.resolve(__dirname,'planner.html'));
await p.pdf({path:path.resolve(__dirname,'讀書計畫手帳.pdf'),format:'A4',printBackground:true});
await b.close();})();
