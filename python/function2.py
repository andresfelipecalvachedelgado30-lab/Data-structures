#function2.py
#function with return and without params       
from random import randint
import os
def roll_dice():
    die1 = randint(1, 6)
    die2 = randint(1, 6)
    return die1, die2
#main 
os.system('clear')
dice=roll_dice()
print(f"Dice : {dice}") 
if dice[0] ==6 and dice[1] ==6:
    print("You win!!")

else:
    print("try again!!") 