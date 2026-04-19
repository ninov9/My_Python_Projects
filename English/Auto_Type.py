from time import sleep
import pynput
from pynput.keyboard import Controller, Key

z = 0
clavier = Controller()
mot = ""  # Word before the number
sleep(5)  # Sleep to give time to focus on the input field

for i in range(101):  # Number of times it will write
    for k in range(len(mot)):
        clavier.tap(mot[k])
        sleep(0.01)
    
    for j in range(len(str(i))):
        clavier.tap(str(i)[j])
        sleep(0.01)
    
    sleep(0.01)
    clavier.tap("%")  # Word after the number
    sleep(1)
    clavier.press(Key.backspace)
    sleep(0.01)
    clavier.press(Key.backspace)
    if z >= 10:
        sleep(0.1)
        clavier.press(Key.backspace)
    sleep(0.5)  # Sleep before the program writes again
    z += 1

