from PIL import Image, ImageDraw, ImageFont
import pystray
import threading
import time

class Tray_display():
    
    icon = None
    exit_callback = None

    def __init__(self):
        self.icon = pystray.Icon('tell_you_when_pc_last_operate')
        self.set_menu()
    
    def set_exit_callback(self, callback_func):
        self.exit_callback = callback_func

    def exit(self):
        print("Exit")
        self.icon.stop()
        if(self.exit_callback):
            self.exit_callback()

    def set_menu(self):
        menu_item = pystray.MenuItem("Exit", lambda icon, item: self.exit())
        self.icon.menu = pystray.Menu(menu_item)
        self.icon.update_menu()
    
    def create_icon_by_text(self, text):
        width = 200
        height = 200
        color1 = 0x000000
        color2 = 0xFFFFFF
        image = Image.new('RGB', (width, height), color1)
        dc = ImageDraw.Draw(image)
        dc.text((0,0),text,font=ImageFont.truetype('C:/Windows/Fonts/Arial.ttf',190),fill = color2)
        self.icon.icon = image

    def run(self):
        self.create_icon_by_text(":)")
        self.icon.title= "监控电脑最后的操作时间"
        self.icon.run()
