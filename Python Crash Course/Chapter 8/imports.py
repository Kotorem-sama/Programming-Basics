def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages:list, sent_messages=[]):
    messages.reverse()
    while messages:
        message = messages.pop()
        sent_messages.append(message)
        show_messages([message])