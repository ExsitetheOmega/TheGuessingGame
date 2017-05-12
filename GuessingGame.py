# Guessing Game
import time
import random
import sys
import os


TheGoodNumber = str(random.randint(1,10))
python = sys.executable

def DrawBoard(x):
    x = str(x)
    if x == TheGoodNumber:
        print("="*30)
        print("=" + " " * 28 + "=")
        print("=" + " " * 28 + "=")
        print("=  Well done you Succeeded!  =")
        print("=  Another round? (yes/no)   =")
        print("=" + " " * 28 + "=")
        print("=" + " " * 28 + "=")
        print("="*30)
        while True:
            AR = input("")
            if AR == "yes":
                os.execl(python, python, * sys.argv)
            elif AR == "no":
                print("Closing game thanks for playing...")
                time.sleep(1)
                quit()
            else:
                print("Try again be sure to type yes or no") 
    else:
        print("="*30)
        print("=" + " " * 28 + "=")
        print("=" + " " * 28 + "=")
        print("=       Nope try again!      =")
        print("=" + " " * 28 + "=")
        print("=" + " " * 28 + "=")
        print("="*30)


login = input("UserName: ")
print("Loading up game...")
time.sleep(0.5)
print("Welcome " + login + "! to the guessing game!")
Okay = True
Chances = 4
while Okay:
    Guess = input("Guess a number from 1 to 10: ")
    DrawBoard(Guess)
    Chances -= 1
    if Chances == 0:
        while True:
            NT = input("You failed!\nTry again? (yes/no)\n ")
            if NT == "yes":
                os.execl(python, python, * sys.argv)
            elif NT == "no":
                print("Closing game thanks for playing...")
                time.sleep(1)
                quit()
            else:
                print("Type again")
    


