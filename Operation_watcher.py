import pyWinhook
import pythoncom
import time

class Operation_watcher:
    
    hook_manager: pyWinhook.HookManager
    last_operate_time: float
    last_operate_name: str

    def user_operate(self, event: pyWinhook.HookEvent):
        interval_time = time.time() - self.last_operate_time
        self.last_operate_time = time.time()
        self.last_operate_name = event.MessageName
        # print(f'{interval_time}: {event.MessageName}')
        return True
    
    def __init__(self):
        self.hook_manager = pyWinhook.HookManager()
        self.hook_manager.KeyAll = self.user_operate
        self.hook_manager.MouseAll = self.user_operate
        self.last_operate_time = time.time()

    def watch(self):
        self.hook_manager.HookKeyboard()
        self.hook_manager.HookMouse()
        pythoncom.PumpMessages()