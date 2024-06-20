print("Modified Problem 3-7: Dinner Guests")
guests = ['julius cesar', 'jon roberts', 'michael corleone']
popped = guests.pop() #Popping off michael
print(f"Sorry {popped.title()} but you're uninvited.") #Letting michael know he cant come
print(f"{guests[0].title()} you're still invited.") 
print(f"{guests[1].title()} you're still invited.")
print("\nList of guests attending: ")
guests.sort()
print(f"{guests[0].title()} and {guests[1].title()}")
print(f"\nNumber of guests coming is:", len(guests))
del guests[1] #Deleting the last few elements
del guests[0]
print(guests) #Prints an empty list 