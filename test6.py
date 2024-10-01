import pygame_gui


temp = float (input("What is the temperature?:"))

if temp>90:
    print ("Temperature is too hot.")
elif temp < 40:
    print ("Temperature is cold.")
else:
    print ("Temperature is fine")
