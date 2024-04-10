import pyautogui
import keyboard

clicking = False


def toggle_clicking():
    global clicking
    clicking = not clicking


def click_mouse():
    pyautogui.click()


keyboard.add_hotkey('f8', toggle_clicking)

while True:
    if clicking:
        click_mouse()
