#!/usr/bin/env python3

#8.OCT.2017
#Esteban

import pyautogui
import random

months = ['j', 'd', 'a', 's', 'm', 'n', 'f','o']

newUsersMail= ['**001@yahoo.es', '**002@yahoo.es', '**003@yahoo.es'
, '**004@yahoo.es', '**005@yahoo.es', '**006@yahoo.es', '**007@yahoo.es'
, '**008@yahoo.es', '**009@yahoo.es', '**010@yahoo.es', '**011@yahoo.es'
, '**012@yahoo.es', '**013@yahoo.es']

for idx, val in enumerate(newUsersMail):
    pyautogui.click(109,972)
    pyautogui.PAUSE=10
    pyautogui.click(301,433)
    pyautogui.PAUSE=1
    pyautogui.click(378,380)
    pyautogui.PAUSE=1
    #First Email
    pyautogui.typewrite(val)
    pyautogui.PAUSE=0.75
    pyautogui.hotkey('tab')
    pyautogui.typewrite(val)
    pyautogui.PAUSE=0.75
    pyautogui.hotkey('tab')
    #Pass
    pyautogui.typewrite('clave123')
    pyautogui.PAUSE=0.75
    pyautogui.hotkey('tab')
    pyautogui.typewrite(val.split('@')[0])
    pyautogui.PAUSE=0.75
    pyautogui.hotkey('tab')
    #Dates
    pyautogui.typewrite(str(random.randint(1,29)))
    pyautogui.PAUSE=0.50
    pyautogui.hotkey('tab')
    pyautogui.typewrite(str(random.choice(months)))
    pyautogui.PAUSE=0.50
    pyautogui.hotkey('tab')
    pyautogui.typewrite(str(random.randint(1990,2000)))
    pyautogui.PAUSE=0.50
    #Male
    pyautogui.hotkey('tab')
    #Female
    pyautogui.hotkey('tab')
    pyautogui.hotkey('space')
    pyautogui.PAUSE=0.50
    pyautogui.hotkey('tab')
    pyautogui.hotkey('space')
    #To the robot
    pyautogui.hotkey('tab')
    pyautogui.PAUSE=1
    pyautogui.hotkey('space')
    #Human Interaction
    pyautogui.PAUSE=20.0
    pyautogui.hotkey('tab')
    pyautogui.PAUSE=0.25
    pyautogui.hotkey('tab')
    pyautogui.PAUSE=0.25
    pyautogui.hotkey('tab')
    pyautogui.PAUSE=0.25
    pyautogui.hotkey('tab')
    pyautogui.PAUSE=0.25
    pyautogui.hotkey('tab')
    pyautogui.PAUSE=0.25
    pyautogui.hotkey('tab')
    pyautogui.PAUSE=0.25
    pyautogui.hotkey('enter')
    pyautogui.scroll(+10)
    pyautogui.scroll(-10)
    pyautogui.PAUSE=3
    pyautogui.scroll(+10)
    pyautogui.scroll(-10)
    pyautogui.hotkey('tab')
    pyautogui.PAUSE=12.0
    pyautogui.hotkey('ctrl', 'w')
    pyautogui.PAUSE=1