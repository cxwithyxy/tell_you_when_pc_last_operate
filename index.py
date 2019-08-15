import threading
import multiprocessing
from Operation_watcher import Operation_watcher
from Web_server import Web_server
from Tray_display import Tray_display
import pythoncom

pipe1, pipe2 = multiprocessing.Pipe()
lock = threading.RLock()

def Tray_display_run(pipe: multiprocessing.Pipe):
    def on_exit():
        pipe.send("exit")
    tray_display = Tray_display()
    tray_display.set_exit_callback(on_exit)
    tray_display.run()

def main_process(pipe: multiprocessing.Pipe):

    def wait_exit_code():
        while True:
            pipe_msg = pipe.recv()
            print(pipe_msg)
            if pipe_msg == "exit":
                operation_watcher.unwatch()
                break

    operation_watcher = Operation_watcher(lock)
    threading.Thread(
        target = operation_watcher.watch,
        daemon = True
    ).start()
    threading.Thread(
        target = Web_server(lock).start,
        args = (operation_watcher,),
        daemon = True
    ).start()
    wait_exit_code()

if __name__ == '__main__':
    multiprocessing.freeze_support()
    p1 = multiprocessing.Process(
        target = Tray_display_run,
        args = (pipe1,)
    )
    p2 = multiprocessing.Process(
        target = main_process,
        args = (pipe2,)
    )
    p1.start()
    p2.start()
    p1.join()
    p2.join()