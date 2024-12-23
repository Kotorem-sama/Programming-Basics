# 7-10. Dream Vacation: Write a program that polls users
# about their dream vacation. Write a prompt similar to If
# you could visit one place in the world, where would you
# go? Include a block of code that prints the results of the
# poll.

responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("If you could visit one place in the world, where would you go? ")
    repeat = input("Would you like to let another person repond? (yes/no) ")
    responses[name] = response

    if repeat == 'no':
        polling_active = False


print('\n--- Poll Results ---')
for name, response in responses.items():
    print(f"{name} would like to visit {response}.")