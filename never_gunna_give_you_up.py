import pyautogui, time

from pyautogui import click, sleep
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
width, height = pyautogui.size()
# print(str(width) + ', ' + str(height))

time.sleep(2)
try:
    pyautogui.moveTo(3000, 1000, duration=0.5)
    pyautogui.click(3000, 1000, duration=1)
    pyautogui.typewrite("never going to give you up!\n")
    pyautogui.moveRel(100, 0, duration=0.2)
    pyautogui.click()
    time.sleep(5.5)
    pyautogui.moveRel(-200, 650, duration=0.5)
    pyautogui.click()
except KeyboardInterrupt:
    print("\nDone")
