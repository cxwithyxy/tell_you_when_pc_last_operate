import pyWinhook, pythoncom
class Operation_watcher:
    
    hook_manager:pyWinhook.HookManager

    def Key_down(self, event):
        print(f'Key:{event.Key}')
        return True
    
    def __init__(self):
        self.hook_manager = pyWinhook.HookManager()
        self.hook_manager.KeyDown = self.Key_down

    def watch(self):
        self.hook_manager.HookKeyboard()
        pythoncom.PumpMessages()
        pass