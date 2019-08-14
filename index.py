import threading
import time
import multiprocessing
from Operation_watcher import Operation_watcher
from Web_server import Web_server
from Tray_display import Tray_display


operation_watcher = Operation_watcher()

def on_exit():
    print(operation_watcher)
    operation_watcher.unwatch()

def Tray_display_run():
    tray_display = Tray_display()
    tray_display.set_exit_callback(on_exit)
    tray_display.run()

if __name__ == '__main__':
    multiprocessing.freeze_support()
    print(operation_watcher)
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