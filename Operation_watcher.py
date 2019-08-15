import pyWinhook
import pythoncom
import time
import threading

class Operation_watcher:
    
    hook_manager: pyWinhook.HookManager
    last_operate_time: float
    last_operate_name: str
    interval_time: float
    lock: threading.RLock

    def user_operate(self, event: pyWinhook.HookEvent):
        with self.lock:
            self.interval_time = time.time() - self.last_operate_time
            self.last_operate_time = time.time()
            self.last_operate_name = event.MessageName
        return True
    
    def __init__(self, lock: threading.RLock):
        self.lock = lock
        self.hook_manager = pyWinhook.HookManager()
        self.hook_manager.KeyAll = self.user_operate
        self.hook_manager.MouseAll = self.user_operate
        self.last_operate_time = time.time()

    def unwatch(self):
        self.hook_manager.UnhookKeyboard()
        self.hook_manager.UnhookMouse()

    def watch(self):
        self.hook_manager.HookKeyboard()
        self.hook_manager.HookMouse()
        pythoncom.PumpMessages()