
def show_messages(messages):
    """Printing all messages"""
    for message in messages:
        print(f"{message}")

def send_messages(messages, sent):
    """Printing and moving messages"""
    while messages:
        current = messages.pop()
        print(f"{current}")
        sent.append(current)

# initializing variables
messages = ['hello world', 'some text', 'more text']
sent = []

# calling functions
show_messages(messages)
send_messages(messages, sent)

# printing contents of the lists
print(f"{messages}")
print(f"{sent}")