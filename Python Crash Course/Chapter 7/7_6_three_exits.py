# 7-6. Three Exits: Write different versions of either
# Exercise 7-4 or 7-5 that do each of the following at least
# once:

# 1) Use a conditional test in the while statement to stop
# the loop.

prompt = "What is your age? \n(Enter 'quit' when you are finished.) "
age = ""

while age != 'quit':
    age = input(prompt)

    if age != 'quit':
        if int(age) < 3:
            print("Your ticket is free.\n")
        elif int(age) <= 12:
            print("Your ticket is $10.\n")
        elif int(age) > 12:
            print("Your ticket is $15.\n")

# 2) Use an active variable to control how long the loop runs.

prompt = "What is your age? \n(Enter 'quit' when you are finished.) "
active = True

while active:
    age = input(prompt)

    if age == 'quit':
        active = False
    else:
        if int(age) < 3:
            print("Your ticket is free.\n")
        elif int(age) <= 12:
            print("Your ticket is $10.\n")
        elif int(age) > 12:
            print("Your ticket is $15.\n")

# 3) Use a break statement to exit the loop when the
# user enters a 'quit' value.

prompt = "What is your age? \n(Enter 'quit' when you are finished.) "
age = ""

while age != 'quit':
    age = input(prompt)

    if age == 'quit':
        break
    if int(age) < 3:
        print("Your ticket is free.\n")
    elif int(age) <= 12:
        print("Your ticket is $10.\n")
    elif int(age) > 12:
        print("Your ticket is $15.\n")