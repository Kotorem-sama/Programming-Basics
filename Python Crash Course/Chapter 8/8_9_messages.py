# 8-9. Messages: Make a list containing a series of short
# text messages. Pass the list to a function called
# show_messages(), which prints each text message.

def show_messages(messages):
    for message in messages:
        print(message)

short_messages = [ "Run!", "Hide!", "Duck!", "Jump!" ]
show_messages(short_messages)