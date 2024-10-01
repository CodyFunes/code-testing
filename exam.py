import tkinter as tk
import random


m = tkinter.Tk()

guess = tkinter.Label(input =("please guess a number between 1-20"))
roll = random.randint(1,20)

if guess == roll and guess >=1 and guess <= 20:
    print("you win")
elif guess != roll and guess >=1 and guess <= 20:
    print("you lose")

else:
    print("Invalid guess")


guess.pack()
m.mainloop()
