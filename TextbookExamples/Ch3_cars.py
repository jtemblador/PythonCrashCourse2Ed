cars =['bmw', 'audi', 'toyota', 'subaru']
cars.sort() #Alphabetical order
print(cars) 
cars.sort(reverse=True) #Reverse Alphabetical order
print(cars) 

cars =['bmw', 'audi', 'toyota', 'subaru']
print("\nOriginal List: ")
print(cars)
print("\nSorted List: ")
print(sorted(cars))
print("\nOriginal List Again: ")
print(cars)

print()#New line 
cars =['bmw', 'audi', 'toyota', 'subaru']
print("Printing a list, reversing, then reversing again.")
print(cars)
cars.reverse()
print(cars) #Reverses order of list
cars.reverse() #setting list back to normal 
print(cars)

print("Getting the length of the list: ")
print(len(cars))