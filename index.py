import threading
import time
from Operation_watcher import Operation_watcher

operation_watcher = Operation_watcher()



def main_wait():
    while True:
        q = input("\n===>:\n")
        if q=="q":
            break
            exit()

def check_last_operate():
    while True:
        interval_time = time.time() - operation_watcher.last_operate_time
        if interval_time > 3:
            print(f'more than {interval_time} no operate')
        time.sleep(1)


threading.Thread(
    target = operation_watcher.watch,
    daemon = True
).start()

threading.Thread(
    target = check_last_operate,
    daemon = True
).start()

main_wait()