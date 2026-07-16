# 系統架構文件 (architecture.md)

## 1. 系統架構圖 (System Architecture)
本系統採用經典的「用戶端 - 後端服務 - 資料庫」三層式 Web 架構：

[瀏覽器 (Client / Swagger UI)] 
       │
       │ (透過 HTTP 傳送 JSON 請求)
       ▼
[後端 API (FastAPI)] ──(使用 PostgreSQL 驅動程式)──► [雲端/本地資料庫 (PostgreSQL)]

## 2. 技術棧 (Technology Stack)
* **後端框架**：FastAPI (Python)
* **資料庫**：PostgreSQL
* **部署平台**：Render (Web Service)
* **互動式文件**：Swagger UI (FastAPI 內建，網址為 `/docs`)

## 3. API 路由設計 (API Endpoints)
後端將提供以下三個核心 API 接口，供前端進行圖書資料的操作：

| HTTP 方法 | 網址 (Route) | 功能說明 | 請求內容 (Request Body) | 成功回應 (Response) |
| :--- | :--- | :--- | :--- | :--- |
| **GET** | `/books` | 取得所有書籍列表 | 無 | `200 OK` (書籍陣列 JSON) |
| **POST** | `/books` | 新增一本書籍 | `{ "title": "...", "author": "...", "published_year": ... }` | `201 Created` (新增成功的書籍 JSON) |
| **DELETE** | `/books/{id}` | 刪除指定 ID 的書籍 | 無 (ID 帶在網址中) | `200 OK` `{ "message": "Book deleted successfully" }` |

## 4. 資料流向說明
1. **讀取資料**：用戶發送 `GET /books` ➔ FastAPI 執行 `SELECT * FROM books` ➔ 資料庫回傳資料 ➔ FastAPI 轉為 JSON 格式回傳給用戶。
2. **寫入資料**：用戶發送 `POST /books` 並附帶書籍資料 ➔ FastAPI 驗證欄位 ➔ 執行 `INSERT INTO...` ➔ 資料庫寫入成功 ➔ FastAPI 回傳新書籍資料與 ID。