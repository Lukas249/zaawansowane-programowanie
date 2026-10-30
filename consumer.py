import os
from time import sleep
from typing import List

from filelock import FileLock

DATA_FILE = "data.txt"
LOCK_FILE = "data.txt.lock"
lock = FileLock(LOCK_FILE, -1)


def parse_task(task_str: str) -> tuple[str, str]:
    task = task_str.strip().split(",")
    return task[0], task[1]


def stringify_tasks(tasks: List[List[str]]) -> str:
    return "\n".join([",".join(task) for task in tasks]) + "\n"


while True:
    task_idx = None

    try:
        with lock:
            with open(DATA_FILE, "r+") as f:
                tasks = [list(parse_task(task_str)) for task_str in f.readlines()]

                line_idx = 0
                while line_idx < len(tasks) and task_idx is None:
                    if tasks[line_idx][1] == "pending":
                        task_idx = line_idx

                    line_idx += 1

                if task_idx is not None:
                    print("Working on task:", tasks[task_idx][0])

                    tasks[task_idx][1] = "in_progress"

                    f.seek(0)
                    f.write(stringify_tasks(tasks))
                    f.truncate()
    except Exception as e:
        print(f"Exception: {e}")

    if task_idx is None:
        sleep(5)
        continue

    sleep(30)

    with lock:

        with open(DATA_FILE, "r+") as f:
            tasks = [list(parse_task(task_str)) for task_str in f.readlines()]
            tasks[task_idx][1] = "done"
            f.seek(0)
            f.write(stringify_tasks(tasks))
            f.truncate()

    print("Done task:", tasks[task_idx][0])
