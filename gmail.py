import pyautogui
import time

link = "https://mail.google.com/mail/u/0/"

pyautogui.press('win')

time.sleep(1)

pyautogui.typewrite("chrome")

time.sleep(1)

pyautogui.press("enter")

time.sleep(1)

pyautogui.typewrite("https://mail.google.com/mail/u/0/")
time.sleep(1)
pyautogui.press("enter")
time.sleep(3)


def do_read():
    pyautogui.press('g')
    pyautogui.press('i')
    time.sleep(2)

    pyautogui.press('x')
    time.sleep(2)
    pyautogui.keyDown('shift')
    pyautogui.press('f10')
    pyautogui.keyUp('shift')
    time.sleep(1)
    pyautogui.press("down")
    time.sleep(1)
    pyautogui.press("down")
    time.sleep(1)
    pyautogui.press("down")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'enter')
    time.sleep(5)
    pyautogui.hotkey('shift', '#')
    time.sleep(2)
    pyautogui.press('g')
    pyautogui.press('i')


for x in range(0,1000000):
    do_read()
    