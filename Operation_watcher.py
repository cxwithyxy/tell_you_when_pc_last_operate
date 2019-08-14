import pyWinhook, pythoncom
class Operation_watcher:
    
    hook_manager: pyWinhook.HookManager

    def user_operate(self, event: pyWinhook.HookEvent):
        print(f'operate: {event.MessageName}')
        return True
    
    def __init__(self):
        self.hook_manager = pyWinhook.HookManager()
        self.hook_manager.KeyAll = self.user_operate
        self.hook_manager.MouseAll = self.user_operate

    def watch(self):
        self.hook_manager.HookKeyboard()
        self.hook_manager.HookMouse()
        pythoncom.PumpMessages()