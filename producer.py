import random

import sqlite3

from get_connection import get_connection


def add_task(cur: sqlite3.Cursor, name: str, status: str):
    cur.execute("INSERT INTO tasks VALUES (NULL, ?, ?)", (name, status))
    con.commit()


con = get_connection("database.db")
cur = con.cursor()
cur.execute("CREATE TABLE  IF NOT EXISTS tasks(id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(200), status VARCHAR(20))")

add_task(cur, f"Task{random.randint(0, 1000)}", "pending")
