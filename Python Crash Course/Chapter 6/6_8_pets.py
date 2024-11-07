# 6-8. Pets: Make several dictionaries, where each dictionary
# represents a different pet. In each dictionary, include the
# kind of animal and the owner’s name. Store these
# dictionaries in a list called pets. Next, loop through your
# list and as you do, print everything you know about each
# pet.

dog = { 'kind' : 'dog', 'owner' : 'Jori' }
cat = { 'kind' : 'cat', 'owner' : 'Luuk' }
gecko = { 'kind' : 'gecko', 'owner' : 'Alisa' }
parrot = { 'kind' : 'parrot', 'owner' : 'Hugo' }

pets = [dog, cat, gecko, parrot]

for pet in pets:
    print(f"{pet['owner']} owns a {pet['kind']}.")