from threading import Thread
from os import system
from time import sleep
import win32api, win32con
import keyboard
import pyautogui

def click():
	win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,x,y,0,0)
	win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,x,y,0,0)
def move(x, y):
	    win32api.SetCursorPos((x,y))

delay = float(input('Delay: '))

x = 0
y = 0
positions = []
insertpressed = False

while True:
	sleep(.05)
	if keyboard.is_pressed('left'):
		x -= 20
		move(pyautogui.position().x - 20, pyautogui.position().y)
	if keyboard.is_pressed('right'):
		x += 20
		move(pyautogui.position().x + 20, pyautogui.position().y)
	if keyboard.is_pressed('down'):
		y += 20
		move(pyautogui.position().x, pyautogui.position().y + 20)
	if keyboard.is_pressed('up'):
		y -= 20
		move(pyautogui.position().x, pyautogui.position().y - 20)
	if keyboard.is_pressed('ctrl') and not insertpressed:
		insertpressed = True
		positions.append((x, y))
	if not keyboard.is_pressed('ctrl') and insertpressed:
		insertpressed = False
	if keyboard.is_pressed('alt'):
		break
if len(positions) == 0:
	exit()
print(positions)
move(pyautogui.position().x + positions[0][0] - x, pyautogui.position().y + positions[0][1] - y)
x = positions[0][0]
y = positions[0][1]

combinations = []

for i in range(2**len(positions)):
	combinations.append('0' * (len(positions) - len(bin(i)[2:])) + bin(i)[2:])

result = ''

for i in range(len(positions)):
	result = result + str(i) + result
end = [0]*len(positions)
for i in result:
	move(pyautogui.position().x + positions[int(i)][0] - x, pyautogui.position().y + positions[int(i)][1] - y)
	x = positions[int(i)][0]
	y = positions[int(i)][1]
	sleep(.05)
	click()
	end[int(i)] += 1
	if keyboard.is_pressed('insert'):
		exit()
	sleep(delay - .05)
for i in range(len(end)):
	if end[i] % 2 == 1:
		move(pyautogui.position().x + positions[i][0] - x, pyautogui.position().y + positions[i][1] - y)
		x = positions[i][0]
		y = positions[i][1]
		click()
		sleep(delay - .05)
