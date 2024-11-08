# 8-10. Sending Messages: Start with a copy of your program
# from Exercise 8-9. Write a function called send_messages()
# that prints each text message and moves each message to a
# new list called sent_messages as it’s printed. After calling
# the function, print both of your lists to make sure the
# messages were moved correctly.

sent_messages = []

def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages:list):
    messages.reverse()
    while messages:
        message = messages.pop()
        sent_messages.append(message)
        show_messages([message])

short_messages = [ "Run!", "Hide!", "Duck!", "Jump!" ]
send_messages(short_messages)
print(f"To-be sent list: {short_messages}\nSent list: {sent_messages}")