import pyautogui as pag
import time


while True:
    time.sleep(1)
    pag.typewrite("This is a Spam Text")
    time.sleep(1)
    pag.press('enter')