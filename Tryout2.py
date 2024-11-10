from random import choice

tries = 0
highest = 0

while tries < 500000:
    numbers_letters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0,
                   'a', 'b', 'c', 'd', 'e']
    
    my_ticket = [2, 9, 'a', 7]
    tries = 1
    winner = [choice(numbers_letters) for i in range(0,4)]

    while my_ticket != winner:
        winner = [choice(numbers_letters) for i in range(0,4)]
        tries += 1

    if tries > highest:
        highest = tries
    
    print(f"Highest tries = {highest}")