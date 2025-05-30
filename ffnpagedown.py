#!/usr/bin/env python3

import pyautogui
pyautogui.FAILSAFE = True
print('Enter the number of pages for the fandom:')
pages = input()
inp = int(pages)
pyautogui.click()
pyautogui.moveRel(1,5)
pyautogui.moveRel(-1,5)
pyautogui.PAUSE = 5
for _ in range(inp + 4):
	pyautogui.press('pagedown')
	pyautogui.PAUSE = 2