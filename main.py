#Code made by Treq. Please leave this credit in :)

from time import sleep
import pyautogui
import keyboard

print("Log: Starting...")
sleep(2)
a = 0
print("Log: Ready")
print("")

while True:
    
    
    if keyboard.is_pressed('c'): #when button c is pressed
        pyautogui.click()   #click
        print("Log: Clicked") 
    
