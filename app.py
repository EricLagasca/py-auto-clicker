import threading
import time
from datetime import datetime

from pynput import keyboard
from pynput.mouse import Button, Controller


class ClickMouse(threading.Thread):
    def __init__(self, button, delay=1):
        super(ClickMouse, self).__init__()
        self.button = button
        self.delay = delay
        self.clicking = False
        self.running = True

    def start_clicking(self):
        self.clicking = True

    def stop_clicking(self):
        self.clicking = False

    def exit(self):
        self.stop_clicking()
        self.running = False

    def run(self):
        while self.running:
            while self.clicking:
                print(f"{datetime.now()} :: Click, click!!!")
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)


mouse = Controller()
click_mouse = ClickMouse(Button.left, 0.01)
click_mouse.start()


def on_activate_i():
    if click_mouse.clicking:
        click_mouse.stop_clicking()
        print(f"{datetime.now()} :: Stopped clicking")
    else:
        click_mouse.start_clicking()
        print(f"{datetime.now()} :: Started clicking")


def on_activate_o():
    click_mouse.exit()
    print(f"{datetime.now()} :: Exited clicker")
    listener.stop()


with keyboard.GlobalHotKeys(
    {
        "<ctrl>+<alt>+i": on_activate_i,
        "<ctrl>+<alt>+o": on_activate_o,
    }
) as listener:
    print(f"{datetime.now()} :: Started listening...")
    listener.join()
