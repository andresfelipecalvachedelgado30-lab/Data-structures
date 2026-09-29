#name script file: loop.py
#this script roll dice ten times 

from random import randint
import os
def roll_dice():
   i=1
   while i<=10:
      key=input("press any key to roll dice: ")
      print(f":::Roll {i} :::")
      print(f"dice1: {randint(1,6)}")
      print(f"dice2: {randint(1,6)}")
      print("\n")
      i+=1
roll_dice()