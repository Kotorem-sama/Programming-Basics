# 9-14. Lottery: Make a list or tuple containing a series
# of 10 numbers and 5 letters. Randomly select 4 numbers or
# letters from the list and print a message saying that any
# ticket matching these 4 numbers or letters wins a prize.

from random import choice

numbers_letters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0,
                   'a', 'b', 'c', 'd', 'e']

winner = [str(choice(numbers_letters)) for i in range(0,4)]
stringified = " ".join(winner)
print(f"Any ticket matching \'{stringified}\' wins a prize!")