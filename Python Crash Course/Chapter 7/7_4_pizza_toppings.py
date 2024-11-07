# 7-4. Pizza Toppings: Write a loop that prompts the user to
# enter a series of pizza toppings until they enter a 'quit'
# value. As they enter each topping, print a message saying
# you’ll add that topping to their pizza.

prompt = "What toppings do you want on your pizza? \n(Enter 'quit' when you are finished.) "

topping = ""

while topping != 'quit':
    topping = input(prompt)

    if topping != 'quit':
        print(topping)