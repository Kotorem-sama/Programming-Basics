# 3-5. Changing Guest List: You just heard that one of your 
# guests can’t make the dinner, so you need to send out a new
# set of invitations. You’ll have to think of someone else to
# invite.

# 1) Start with your program from Exercise 3-4. Add a print()
# call at the end of your program, stating the name of the
# guest who can’t make it.
guests = ["Michael Jackson","Freddy Mercury","Robbert Topala"]
print(f"{guests[2]} can't make it")

# 2) Modify your list, replacing the name of the guest who
# can’t make it with the name of the new person you
# are inviting.
guests[2] = "Steve Jobs"

# 3) Print a second set of invitation messages, one for each
# person who is still in your list.
print(f"Hey {guests[0]}. You're invited to dine with me.")
print(f"Hey {guests[1]}. You're invited to dine with me.")
print(f"Hey {guests[2]}. You're invited to dine with me.")