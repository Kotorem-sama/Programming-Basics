# 3-6. More Guests: You just found a bigger dinner table,
# so now more space is available. Think of three more
# guests to invite to dinner.

# 1) Start with your program from Exercise 3-4 or 3-5. Add a
# print() call to the end of your program, informing people
# that you found a bigger table.

guests = ["Michael Jackson","Freddy Mercury","Steve Jobs"]

print(f"Hey {guests[0]}. I found a bigger table.")
print(f"Hey {guests[1]}. I found a bigger table.")
print(f"Hey {guests[2]}. I found a bigger table.")
print()

# 2) Use insert() to add one new guest to the beginning
# of your list

guests.insert(0, "Ariana Grande")

# 3) Use insert() to add one new guest to the middle of
# your list.

guests.insert(len(guests)//2, "Steven King")

# 4) Use append() to add one new guest to the end of
# your list.

guests.append("Matt Mathews")

# 5) Print a new set of invitation messages, one for each
# person in your list.

print(f"Hey {guests[0]}. You're invited to dine with me.")
print(f"Hey {guests[1]}. You're invited to dine with me.")
print(f"Hey {guests[2]}. You're invited to dine with me.")
print(f"Hey {guests[3]}. You're invited to dine with me.")
print(f"Hey {guests[4]}. You're invited to dine with me.")
print(f"Hey {guests[5]}. You're invited to dine with me.")