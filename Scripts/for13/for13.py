#!/usr/bin/env python3

#Update 16.OCT
#7.OCT.2017
#Esteban

import pyautogui
users = ['**001', '**002', '**003', '**004', '**005','**006','**007','**008','**009','**010','**011','**012','**013']
total = len(users) + 1

for x in range(total):
    pyautogui.click(86, 975)
    pyautogui.PAUSE=2
for x in users:
    pyautogui.PAUSE=8
    pyautogui.click(558, 388)
    pyautogui.hotkey('ctrl','a')
    pyautogui.PAUSE=1.75
    pyautogui.typewrite(x)
    pyautogui.press('tab')
    pyautogui.typewrite('clave123')
    pyautogui.press('enter')
    pyautogui.PAUSE=14
    pyautogui.click(688,909)
    #Click repeat
    pyautogui.click(670,909)
    #Shuffle
    pyautogui.click(464, 909)
    pyautogui.PAUSE=3
    #Playlist
    pyautogui.doubleClick(48, 407)
    pyautogui.click(900, 22)
    pyautogui.click(1052, 14)