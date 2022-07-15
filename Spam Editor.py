from tkinter.messagebox import YES
import pyautogui
import time
from datetime import date 
import datetime
import os
e = datetime.datetime.now()
print("-------------------------------------------------------------------------")
Question = input("""What Would You Like To Do?
1. Start the spam CountDown
2. Edit the .txt file
3. Close Spam.exe
-------------------------------------------------------------------------
""")

if Question == ("3"):
  open.close()

if Question == ("2"):
  os.system('config.txt')

if Question == ("1"):
  print('5')
  time.sleep(1)
  print('4')
  time.sleep(1)
  print('3')
  time.sleep(1)
  print('2')
  time.sleep(1)
  print('1')
  time.sleep(1)
  print('0')

file = open("Config.txt", 'r')
for word in file:
  pyautogui.typewrite(word)
  time.sleep(.300)
  pyautogui.press('enter')
  print("[BOT] At",e.strftime("%H:%M %p:"), word)


