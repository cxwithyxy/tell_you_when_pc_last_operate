import threading
import time
import multiprocessing
from Operation_watcher import Operation_watcher
from Web_server import Web_server
from Tray_display import Tray_display


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

def Tray_display_run():
    Tray_display().run()


if __name__ == '__main__':
    multiprocessing.freeze_support()
    
    p1 = multiprocessing.Process(
        target = Tray_display_run,
        daemon = True
    )
    
    threading.Thread(
        target = operation_watcher.watch,
        daemon = True
    ).start()
     
    threading.Thread(
        target = Web_server().start,
        args = (operation_watcher,),
        daemon = True
    ).start()
    p1.start()
    p1.join()
    # main_wait()
