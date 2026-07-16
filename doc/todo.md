# 開發待辦清單 (todo.md)

- [ ] **階段 1：環境設定與套件安裝**
  - [ ] 1.1 確認 Python 虛擬環境 (`venv`) 處於啟用狀態
  - [ ] 1.2 安裝 PostgreSQL 連線驅動套件：`pip install psycopg2-binary`
  - [ ] 1.3 更新套件清單檔案：執行 `pip freeze > requirements.txt`

- [ ] **階段 2：資料庫連線程式碼實作 (Database Connection)**
  - [ ] 2.1 在 `main.py` 中導入 `psycopg2` 模組
  - [ ] 2.2 撰寫資料庫連線函式，讀取本地端與 Render 雲端環境變數
  - [ ] 2.3 測試資料庫連線，若連線失敗時輸出清楚的錯誤訊息

- [ ] **階段 3：API 路由功能開發 (Routes)**
  - [ ] 3.1 實作 `GET /books`：從 PostgreSQL 查詢所有書籍並回傳為 JSON
  - [ ] 3.2 實作 `POST /books`：接收 JSON 參數，將新書籍寫入資料庫，並回傳新資料
  - [ ] 3.3 實作 `DELETE /books/{id}`：根據網址傳入的 ID，從資料庫中刪除對應的書籍

- [ ] **階段 4：本地測試與除錯 (Local Testing)**
  - [ ] 4.1 啟動 FastAPI 服務 (`uvicorn main:app --reload`)
  - [ ] 4.2 開啟網頁 `http://127.0.0.1:8000/docs` (Swagger UI)
  - [ ] 4.3 測試「新增書籍 API」➔ 確認 pgAdmin 中的資料表有同步增加
  - [ ] 4.4 測試「查詢書單 API」➔ 確認能回傳完整的 JSON 陣列
  - [ ] 4.5 測試「刪除書籍 API」➔ 確認資料成功被刪除

- [ ] **階段 5：雲端部署與驗證 (Deployment)**
  - [ ] 5.1 使用 Git 將更新提交並推送到 GitHub 儲存庫
  - [ ] 5.2 登入 Render 平台，確認服務自動觸發構建與部署
  - [ ] 5.3 測試線上的專屬 API 網址，驗證功能全部正常運作