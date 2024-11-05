# 3-7. Shrinking Guest List: You just found out that your new
# dinner table won’t arrive in time for the dinner, and now
# you have space for only two guests.

# 1) Start with your program from Exercise 3-6. Add a new line
# that prints a message saying that you can invite only two
# people for dinner

guests = ['Ariana Grande', 'Michael Jackson', 'Steven King',
          'Freddy Mercury', 'Steve Jobs', 'Matt Mathews']

print(f"Hey {guests[0]}. I can only invite 2 people.")
print(f"Hey {guests[1]}. I can only invite 2 people.")
print(f"Hey {guests[2]}. I can only invite 2 people.")
print(f"Hey {guests[3]}. I can only invite 2 people.")
print(f"Hey {guests[4]}. I can only invite 2 people.")
print(f"Hey {guests[5]}. I can only invite 2 people.")
print()

# 2) Use pop() to remove guests from your list one at a time
# until only two names remain in your list. Each time you
# pop a name from your list, print a message to that person
# letting them know you’re sorry you can’t invite them
# to dinner.

print(f"Hey {guests.pop(1)}. Sorry. I can't invite you to dinner.")
print(f"Hey {guests.pop(3)}. Sorry. I can't invite you to dinner.")
print(f"Hey {guests.pop(0)}. Sorry. I can't invite you to dinner.")
print(f"Hey {guests.pop(2)}. Sorry. I can't invite you to dinner.")
print()

# 3) Print a message to each of the two people still on
# your list, letting them know they’re still invited.

print(f"Hey {guests[0]}. You're still invited.")
print(f"Hey {guests[1]}. You're still invited.")
print()

# Use del to remove the last two names from your list, so you
# have an empty list. Print your list to make sure you actually
# have an empty list at the end of your program.

del guests[0]
del guests[0]
print(guests)