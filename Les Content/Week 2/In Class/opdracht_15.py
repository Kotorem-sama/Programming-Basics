# 15. 
# a. Schrijf een programma met twee functies: roll_dice() en display(dice),
# die het gooien van 2 dobbelstenen simuleert.
# b. Blijf de dobbelstenen gooien tot het totaal een 7 is.

import random

def roll_dice():
    return random.randint(1, 6)

def display(dice):
    total = 0
    while dice > 0:
        dice -= 1
        total += roll_dice()
    
    return total

print(display(2))