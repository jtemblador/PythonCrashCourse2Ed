responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb today? ")

    # Store reponse in a dictionary 
    responses[name] = response

    # find out if anyone else is going to take the poll
    repeat = input("Any more taking poll? ")
    if repeat == 'no':
        polling_active = False

print("\n---Polling Results--")
for name, response in responses.items():
    print(f"{name} wants to climb {response}")