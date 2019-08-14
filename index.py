import threading
from Operation_watcher import Operation_watcher


threading.Thread(
    target = Operation_watcher().watch,
    daemon = True
).start()


def main_wait():
    while True:
        q = input("\n===>:\n")
        if q=="q":
            break
            exit()


main_wait()