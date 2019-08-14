import pyWinhook, pythoncom

def OnKeyboardEvent(event):
    print(f'Key:{event.Key}')
    return True

hm = pyWinhook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()


pythoncom.PumpMessages()