# 8-11. Archived Messages: Start with your work from Exercise
# 8-10. Call the function send_messages() with a copy of the
# list of messages. After calling the function, print both of
# your lists to show that the original list has retained its
# messages.

def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    messages.reverse()
    while messages:
        message = messages.pop()
        sent_messages.append(message)
        show_messages([message])

sent_messages = []
short_messages = [ "Run!", "Hide!", "Duck!", "Jump!" ]
send_messages(short_messages[:], sent_messages)
print(f"Archive: {short_messages}\nSent list: {sent_messages}")