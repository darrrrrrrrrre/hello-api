# 資料模型文件 (data-model.md)

## 1. 資料表設計：books (書籍表)
這是我們用來存放書籍資料的主要資料表。

| 欄位名稱 (Column) | 資料類型 (Type) | 主鍵 (PK) | 允許空值 (Null) | 預設值 (Default) | 說明 (Description) |
| :--- | :--- | :---: | :---: | :--- | :--- |
| **id** | SERIAL | 是 (PK) | 否 | 自動遞增 | 書籍唯一識別碼 (自動生成) |
| **title** | VARCHAR(255) | 否 | 否 | 無 | 書名 (必填欄位) |
| **author** | VARCHAR(100) | 否 | 否 | 無 | 作者姓名 (必填欄位) |
| **published_year** | INTEGER | 否 | 是 | NULL | 出版年份 (選填) |

## 2. 資料庫初始化 SQL 語法 (DDL)
這是在 PostgreSQL 建立此資料表的標準語句：

```sql
CREATE TABLE IF NOT EXISTS books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(100) NOT NULL,
    published_year INTEGER
);