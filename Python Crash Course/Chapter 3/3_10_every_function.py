# 3-10. Every Function: Think of things you could store in a
# list. For example, you could make a list of mountains,
# rivers, countries, cities, languages, or anything else
# you’d like. Write a program that creates a list containing
# these items and then uses each function introduced in this
# chapter at least once.

# Make list
languages = ["Not a language"]

# Change list item
languages[0] = "English"

# Add item to end of list
languages.append("Dutch")

# Add item at a specified position in list
languages.insert(1, "Bull")

# Remove item at a specified position in list
del languages[1]

# Add items from list to list
languages.extend(["Bull1", "Bull2", "Bull3"])

# Remove item at a specified position in list
languages.pop(3)

# Remove item at the end of list
languages.pop()

# Remove 1st instance of specific item from list
languages.remove("Bull1")

# Adds more to make next thing easier to see
languages.extend(["Spanish", "German", "Finnish"])

# Sort list without changing list
print(sorted(languages))
print(languages)

# Reverse sort list without changing liist
print(sorted(languages, reverse=True))
print(languages)

# Reverse a list
languages.reverse()

# Sort list
languages.sort()

# Reverse sort list
languages.sort(reverse=True)

# Get length of list
print(len(languages))