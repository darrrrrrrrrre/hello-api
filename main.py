import sqlite3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# 1. 直接指定一個本地檔案作為資料庫 (完全不需要帳號密碼！)
DB_FILE = "local_books.db"

def init_db():
    # 自動建立 books 資料表
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            published_year INTEGER
        );
    """)
    # 順便塞一筆測試資料，讓妳等一下有東西看
    cur.execute("SELECT COUNT(*) FROM books;")
    if cur.fetchone()[0] == 0:
        cur.execute("INSERT INTO books (title, author, published_year) VALUES ('測試書籍', '測試作者', 2026);")
    conn.commit()
    conn.close()

# 啟動時自動幫妳初始化資料庫檔案
init_db()

class BookCreate(BaseModel):
    title: str
    author: str
    published_year: int = None

@app.get("/")
def read_root():
    return {"status": "ok", "message": "SQLite 圖書管理 API 運作中"}

# 2. 查詢書單
@app.get("/books")
def get_all_books():
    conn = sqlite3.connect(DB_FILE)
    # 讓查詢結果自動變成字典格式，方便轉成 JSON
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    try:
        cur.execute("SELECT id, title, author, published_year FROM books ORDER BY id DESC;")
        books = [dict(row) for row in cur.fetchall()]
        return books
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

# 3. 新增書籍
@app.post("/books", status_code=201)
def create_book(book: BookCreate):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO books (title, author, published_year) VALUES (?, ?, ?);",
            (book.title, book.author, book.published_year)
        )
        new_id = cur.lastrowid
        conn.commit()
        return {"id": new_id, "title": book.title, "author": book.author, "published_year": book.published_year}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

# 4. 刪除書籍
@app.delete("/books/{id}")
def delete_book(id: int):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM books WHERE id = ?;", (id,))
        if cur.rowcount == 0:
            raise HTTPException(status_code=404, detail="找不到該 ID 的書籍")
        conn.commit()
        return {"message": f"成功刪除 ID 為 {id} 的書籍"}
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()