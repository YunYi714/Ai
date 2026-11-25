# 租屋權益站

台灣租屋族權益查詢與免費試算工具（靜態網站，GitHub Pages）。

- `docs/`：網站成品（GitHub Pages 發布這個資料夾）
- `src/`：原始碼。修改後執行 `python3 src/build.py` 重新產生 `docs/`
  - `src/tools/`：計算工具（每個檔案一個工具）
  - `src/guides/`：權益懶人包
  - `src/config.py`：網站名稱、網址、AdSense ID

## 上線步驟
1. GitHub → Settings → Pages → Source: Deploy from a branch → Branch 選 `main`、資料夾 `/docs` → Save
2. 網站網址：https://yunyi714.github.io/Ai02/
3. 到 Google Search Console 提交 `sitemap.xml`
4. 申請 AdSense 後把 `ca-pub-...` 填入 `src/config.py` 的 `ADSENSE_CLIENT`，重新 build

## 內容
- 工具：租屋權益健檢、電費檢查、押金違約金檢查、租金報稅試算、室友分攤
- 懶人包：押金、電費、報稅與戶籍、修繕、提前解約與漲租、隱私、爭取權益的方法
