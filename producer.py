import random

from filelock import FileLock

DATA_FILE = "data.txt"
LOCK_FILE = "data.txt.lock"
lock = FileLock(LOCK_FILE, -1)

with lock:
    with open(DATA_FILE, "a") as f:
        f.write(f"Task{random.randint(0, 1000)},pending\n")
