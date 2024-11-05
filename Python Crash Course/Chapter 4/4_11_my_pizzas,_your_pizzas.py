# 4-11. My Pizzas, Your Pizzas: Start with your program from
# Exercise 4-1 (page 56). Make a copy of the list of pizzas,
# and call it friend_pizzas. Then, do the following:

pizzas = ["Margarita", "Fungi", "Pepperoni"]
friend_pizzas = pizzas[:]

# 1) Add a new pizza to the original list.

pizzas.append("Hawaii")

# 2) Add a different pizza to the list friend_pizzas.

friend_pizzas.append("BBQ Mixed Grill")

# 3) Prove that you have two separate lists. Print the
# message My favorite pizzas are:, and then use a for loop
# to print the first list. Print the message My friend’s
# favorite pizzas are:, and then use a for loop to print the
# second list. Make sure each new pizza is stored in the
# appropriate list.

print(f"My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)