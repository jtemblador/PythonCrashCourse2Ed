print("Chapter 3 Problem 3-4: Guest List")
#creating list of guests
guests = ['john lennon', 'jake gyllenhaal', 'bob']
#inviting each one to dinner
print(f"Would you like to come to dinner, {guests[0].title()}?")
print(f"{guests[1].title()}, would you like to come to dinner?")
print(f"Will you be coming to dinner {guests[2].title()}?")
print(f"Guest list is {guests}")

print("\nChapter 3 Problem 3-5: Changing Guest List")
#removing/adding someone to list
del guests[0] #deletes john lennon
guests.insert(0, 'yoda') #adding yoda
#inviting each one to dinner
print(f"Would you like to come to dinner, {guests[0].title()}?")
print(f"{guests[1].title()}, would you like to come to dinner?")
print(f"Will you be coming to dinner {guests[2].title()}?")
print(f"Guest list is {guests}")

print("\nChapter 3 Problem 3-6: More Guests")
print("Only two people can be ivited for dinner.")
#removing yoda from list
print(f"Sorry {guests.pop(0).title()}, but you must be a Human in order to come.")
#letting know the two guests are still invited
print(f"{guests[0].title()}, you're still invited.")
print(f"{guests[1].title()}, you're still invited.")
#deleting then printing list to make sure it's empty
del guests[0]
guests.remove('bob')
#printing empty list
print(guests)

print("\nChapter 3 Problem 3-7: More Guests")
guests = ['julius cesar', 'jon roberts', 'michael corleone']
popped = guests.pop() #Popping off michael
print(f"Sorry {popped.title()} but you're uninvited.") #Letting michael know he cant come
print(f"{guests[0].title()} you're still invited.") 
print(f"{guests[1].title()} you're still invited.")
del guests[1] #Deleting the last few elements
del guests[0]
print(guests) #Prints an empty list 