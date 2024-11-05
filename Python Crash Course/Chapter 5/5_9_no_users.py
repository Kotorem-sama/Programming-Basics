# 5-9. No Users: Add an if test to hello_admin.py to make sure
# the list of users is not empty.

# 1) If the list is empty, print the message We need to find
# some users!
# 2) Remove all of the usernames from your list, and make
# sure the correct message is printed.

users = []

if users:
    for user in users:
        if user == 'admin':
            print(f"Hello {user}, would you like to see a status report?")
        else:
            print(f"Hello, {user}, thank you for logging in again.")
else:
    print("We need to find some users!")