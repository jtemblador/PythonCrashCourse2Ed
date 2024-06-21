bicycles = ['trek ', 'cannondale', 'redline', 'specialized'] #Creating a list
print(f"{bicycles[0].title().rstrip()} and {bicycles[1]}")   #Printing parts of the list

#Print the last item in list
print(bicycles[-1])
message = f"My first bicycle was a {bicycles[1].title()}"
print(message)

#------------------------------------------------------------------------------------------
#Problem 3-1
print('\nStart of Problem 3-1')
names = ['Jason', 'matthew', 'david', 'Mark']
print(names[0])
print(names[1])
print(names[2])
print(names[3]) 

#Problem 3-2
print('\nStart of Problem 3-2')
print(f"{names[0].title()}, when was the last time you showered?")
print(f"{names[1].title()}, when was the last time you showered?")
print(f"{names[2].title()}, when was the last time you showered?")
print(f"{names[3].title()}, when was the last time you showered?")

#Problem 3-3
print('\nStart of Problem 3-3')
vhcls = ['plane', 'tank', 'submarine', 'car']
message0 = f"Riding in a {vhcls[0]} is fun!"
print(message0)
message1 = f"{vhcls[1].title()}s should be driven in public like {vhcls[3]}s"
print(message1)
message2 = f"Know where I can buy a {vhcls[2]}? It's for the wife."
print(message2)