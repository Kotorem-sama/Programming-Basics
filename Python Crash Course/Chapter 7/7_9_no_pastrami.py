# 7-9. No Pastrami: Using the list sandwich_orders from
# Exercise 7-8, make sure the sandwich 'pastrami' appears
# in the list at least three times. Add code near the
# beginning of your program to print a message saying the
# deli has run out of pastrami, and then use a while loop
# to remove all occurrences of 'pastrami' from
# sandwich_orders. Make sure no pastrami sandwiches end up
# in finished_sandwiches.

sandwich_orders = [ "Chicken Teriyaki", "Pastrami",
                   "Italian B.M.T.", "Pastrami",
                   "Spicy Italian", "Subway Melt",
                   "Pastrami" ]
finished_sandwiches = []

print("The deli has run out of pastrami.")

while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

while sandwich_orders:
    finished_sandwiches.append(sandwich_orders.pop())
    print(f"I made your {finished_sandwiches[-1]}")

sandwich_list = ", ".join(finished_sandwiches)

print(f"Finished sandwiches: {sandwich_list}")