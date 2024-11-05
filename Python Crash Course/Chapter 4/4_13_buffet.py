# 4-13. Buffet: A buffet-style restaurant offers only five
# basic foods. Think of five simple foods, and store them
# in a tuple.

buffet = ("Chicken", "Beef", "Burger", "Salad", "Pizza")

# 1) Use a for loop to print each food the restaurant offers.

for food in buffet:
    print(food)
print()

# 2) Try to modify one of the items, and make sure that
# Python rejects the change.

# buffet[0] = "Vegan Options"

# 3) The restaurant changes its menu, replacing two of the
# items with different foods. Add a line that rewrites the
# tuple, and then use a for loop to print each of the items
# on the revised menu.

buffet = ("Chicken", "Beef", "Kapsalon", "Salad", "Pasta")
for food in buffet:
    print(food)
