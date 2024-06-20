beatles = {
    'john' : '1',
    'paul' : '2',
    'george' : '3',
    'ringo' : '4'
}

#Cycling through dictionary using a for loop
for person in beatles:
    print(f"{person.title()}'s favorite number is {beatles[person]}")

