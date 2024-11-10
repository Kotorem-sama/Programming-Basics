# 9-13. Dice: Make a class Die with one attribute called
# sides, which has a default value of 6. Write a method
# called roll_die() that prints a random number between 1 and
# the number of sides the die has. Make a 6-sided die and roll
# it 10 times.

import random

class Dice:
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_die(self):
        print(random.randint(1,self.sides))

dice_of_6 = Dice()
print("The dice with 6 sides gets rolled:")
for roll in range(0,10):
    dice_of_6.roll_die()

# Make a 10-sided die and a 20-sided die. Roll each die 10
# times.

dice_of_10 = Dice(10)
dice_of_20 = Dice(20)

for dice in [dice_of_10, dice_of_20]:
    print(f"\nThe dice of {dice.sides} gets rolled:")
    for roll in range(0,10):
        dice.roll_die()