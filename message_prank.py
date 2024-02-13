import random
import pyautogui as pg

a=["big","smart","perfect chunk","Chocolate boy"," proo coder","handsome hunk"]

for i in range(200):
    pg.write("pranit u are "+random.choice(a))
    pg.press("Enter")


