import pyautogui
import keyboard
import time

clicking = False


def toggle_clicking():
    global clicking
    clicking = not clicking


def click_mouse():
    pyautogui.click()


keyboard.add_hotkey('f8', toggle_clicking)

while True:
    time.sleep(0.005)
    if clicking:
        click_mouse()
