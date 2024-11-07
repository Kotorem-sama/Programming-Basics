# 6-6. Polling: Use the code in favorite_languages.py
# (page 96).

favorite_numbers = {
    'Tirsa' : 500000001,
    'Rick' : 89,
    'Nick' : 69,
    'Luuk' : 420,
    'Alisa' : 5
}

# 1) Make a list of people who should take the favorite
# languages poll. Include some names that are already in
# the dictionary and some that are not.

poll = { 'Moe', "Boris", "Rick", "Tirsa", "Tobias", "Michelle" }

# 2) Loop through the list of people who should take the poll.
# If they have already taken the poll, print a message
# thanking them for responding. If they have not yet taken
# the poll, print a message inviting them to take the poll.

for person in poll:
    if person in favorite_numbers:
        print(f"{person}, thank you for taking the poll.")
    else:
        print(f"{person}, please take our poll!")