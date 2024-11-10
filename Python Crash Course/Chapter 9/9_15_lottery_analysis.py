# 9-15. Lottery Analysis: You can use a loop to see how hard
# it might be to win the kind of lottery you just modeled.
# Make a list or tuple called my_ticket. Write a loop that
# keeps pulling numbers until your ticket wins. Print a
# message reporting how many times the loop had to run to
# give you a winning ticket.

from random import choice

numbers_letters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0,
                   'a', 'b', 'c', 'd', 'e']

my_ticket = [2, 9, 'a', 7]
tries = 1
winner = [choice(numbers_letters) for i in range(0,4)]

while my_ticket != winner:
    winner = [choice(numbers_letters) for i in range(0,4)]
    tries += 1

print(f"It took me {tries} tries to win the lottery.")