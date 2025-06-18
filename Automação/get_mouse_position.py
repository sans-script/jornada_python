import pyautogui
import mouse

while True:
    print(pyautogui.position())
    if mouse.is_pressed(button='left'):
        break
