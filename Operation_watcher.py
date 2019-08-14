import pyWinhook, pythoncom
class Operation_watcher:

    def OnKeyboardEvent(self, event):
        print(f'Key:{event.Key}')
        return True
    

    def watch(self):
        hm = pyWinhook.HookManager()
        hm.KeyDown = self.OnKeyboardEvent
        hm.HookKeyboard()
        pythoncom.PumpMessages()
        pass