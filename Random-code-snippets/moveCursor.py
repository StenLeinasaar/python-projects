from time import time
import pyautogui as pag
import random
import time
import sys

while True: 
    x = random.randint(200, 1000)
    y =  random.randint(100, 900)
    pag.moveTo(x, y)
    time.sleep(0.5)

