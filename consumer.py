import sqlite3
from time import sleep

from get_connection import get_connection


def get_first_pending_task(cur: sqlite3.Cursor) -> tuple[int, str, str]:
    cur.execute("SELECT id, name, status FROM tasks where status = 'pending' LIMIT 1")
    return cur.fetchone()


while True:

    con = get_connection("database.db")

    task = None

    try:
        cur = con.cursor()
        task = get_first_pending_task(cur)
        cur.execute("UPDATE tasks SET status = 'in_progress' WHERE id = ? AND status = 'pending'", (task[0],))
        con.commit()
    except Exception as e:
        print("Brak zadań")
    finally:
        con.close()

    if task is None:
        sleep(5)
        continue

    print("Working on task:", f"ID: {task[0]}", f"TASK NAME: {task[1]}")

    sleep(30)

    con = get_connection("database.db")

    try:
        cur = con.cursor()
        cur.execute("UPDATE tasks SET status = 'done' WHERE id = ?", (task[0],))
        con.commit()
    except Exception as e:
        print(e)
    finally:
        con.close()

    print("Done task:", f"ID: {task[0]}", f"TASK NAME: {task[1]}")
