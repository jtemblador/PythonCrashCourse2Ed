places = ['moscow', 'sapporo', 'pyongyang', 'manchester', 'cairo']
print("List of places I wanna visit: ")
print(places)

print("\nList of places in alphabetical order: ")
print(sorted(places))

print("Same list: ")
print(places)

print("\nList in alphabetical oder but reversed: ")
print(sorted(places, reverse=True))

print("Same list: ")
print(places)

print("\nSame list but reversed: ")
places.reverse()
print(places)
places.reverse()

print("Same list: ")
print(places)

print("\nSorted List in alphabetical: ")
places.sort()
print(places)

print("\nReverse alphabetically sorted List: ")
places.sort(reverse=True)
print(places)
