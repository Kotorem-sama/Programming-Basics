# 4-10. Slices: Using one of the programs you wrote in this
# chapter, add several lines to the end of the program that
# do the following:

cubes = list(number**3 for number in range(1, 11))

# 1) Print the message The first three items in the list
# are:. Then use a slice to print the first three items
# from that program’s list.
first = ", ".join(str(i) for i in cubes[:3])
print(f"The first three items in the list are: {first}")

# 2) Print the message Three items from the middle of the
# list are:. Then use a slice to print three items from
# the middle of the list.
middle = ", ".join(str(i) for i in cubes[3:6])
print(f"Three items from the middle of the list are: {middle}")

# 3) Print the message The last three items in the list are:.
# Then use a slice to print the last three items in the list.
last = ", ".join(str(i) for i in cubes[-3:])
print(f"The last three items in the list are: {last}")