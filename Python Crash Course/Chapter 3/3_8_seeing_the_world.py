# 3-8. Seeing the World: Think of at least five places in the
# world you’d like to visit.

# 1) Store the locations in a list. Make sure the list is not
# in alphabetical order.

locations = ["Rome", "Czechia", "Greece", "Portugal", "Malta"]

# 2) Print your list in its original order. Don’t worry about
# printing the list neatly; just print it as a raw Python list.

print(locations)

# 3) Use sorted() to print your list in alphabetical order
# without modifying the actual list.

print(sorted(locations))

# 4) Show that your list is still in its original order by
# printing it.

print(locations)

# 5) Use sorted() to print your list in reverse-alphabetical
# order without changing the order of the original list.

print(sorted(locations, reverse=True))

# 6) Show that your list is still in its original order by
# printing it again.

print(locations)

# 7) Use reverse() to change the order of your list. Print the
# list to show that its order has changed.

locations.reverse()
print(locations)

# 8) Use reverse() to change the order of your list again.
# Print the list to show it’s back to its original order.

locations.reverse()
print(locations)

# 9) Use sort() to change your list so it’s stored in
# alphabetical order. Print the list to show that its order
# has been changed.

locations.sort()
print(locations)

# 10) Use sort() to change your list so it’s stored in
# reverse-alphabetical order. Print the list to show that its
# order has changed.

locations.sort(reverse=True)
print(locations)