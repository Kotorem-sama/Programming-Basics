# 5-10. Checking Usernames: Do the following to create a
# program that simulates how websites ensure that everyone
# has a unique username.

# 1) Make a list of five or more usernames called
# current_users.

current_users = ["kotorem_sama", "rickyman2002",
                 "foxy_fright", "coach_knip", "rikkumoist"]

# 2) Make another list of five usernames called new_users.
# Make sure one or two of the new usernames are also in the
# current_users list.

new_users = ["Foxy_fright", "rikkumoistw", "all_mighto",
              "coach_knip", "gaienne"]

# 3) Loop through the new_users list to see if each new
# username has already been used. If it has, print a message
# that the person will need to enter a new username. If a
# username has not been used, print a message saying that
# the username is available.
# 4) Make sure your comparison is case insensitive. If 'John'
# has been used, 'JOHN' should not be accepted. (To do this,
# you’ll need to make a copy of current_users containing the
# lowercase versions of all existing users.)

for user in new_users:
    if user.lower() in current_users:
        print(f"{user} is already in use. Please enter a new username.")
    else:
        print(f"{user} is available")