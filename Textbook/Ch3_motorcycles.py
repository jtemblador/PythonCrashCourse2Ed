mtrcyls = ['honda', 'yamaha', 'suzuki']
print(mtrcyls)
mtrcyls.append('ducati') #adding element to end of the list
print(mtrcyls)	

#adding multiple elements to end of array
stuff = []
stuff.append('honda') 
stuff.append('yamaha')
stuff.append('suzuki')
stuff.insert(0, 'ducati') #inserts 'ducati' into the 0 position element 
print(stuff)

#Deleting element from list
del mtrcyls[-1] #deletes 'ducati'
print(mtrcyls) 

#popping off last element of mtrcyls
pop_mtrcyls = mtrcyls.pop()
print(f"\nLast motorcycle I owned was a {pop_mtrcyls.title()}.")
print(f"List without last element: {mtrcyls}")
mtrcyls.append(pop_mtrcyls) #Putting element back into list
print(f"Original list: {mtrcyls}")

#popping off first element of mtrcyls
first_mtrcyls = mtrcyls.pop(0)
print (f"\nFirst motorcycle I owned was a {first_mtrcyls.title()}.")
print(f"List without first element: {mtrcyls}")
mtrcyls.insert(0, first_mtrcyls) #putting element back in list, adds to end of list
print (f"Original list: {mtrcyls}")

#removing element in list
mtrcyls = ['honda', 'yamaha', 'suzuki', 'ducati']
print(f"\nList of motorcycls {mtrcyls}.")
mtrcyls.remove('ducati') #removed ducati from list 
print(f"Ducati removed {mtrcyls}.")
mtrcyls.append('ducati') #putting ducati back in list

#another way of removing an element from a list
print(f"\nList of motorcycles: {mtrcyls}")
remove = 'ducati' #remove set to ducati
mtrcyls.remove(remove) #removing ducati from list
print(f"New list of motorcycles {mtrcyls}") #printing list 
print(f"{remove.title()} is too expensive for me.")

###############################################
##Chapter 3 problems located in Ch3_Guests.py##
###############################################




