
beatles = {
    'john' :   { 'num1' : 1, 'num2' : 22, 'num3' : 234 },
    'paul' :   { 'num1' : 9, 'num2' : 53, 'num3' : 121 },
    'george' : { 'num1' : 3, 'num2' : 67, 'num3' : 224 },
    'ringo' :  { 'num1' : 4, 'num2' : 93, 'num3' : 876 },
}

#Cycling through dictionary using a for loop
for person, nums in beatles.items():
    print(f"{person.title()}'s first  favorite number is {nums['num1']}")
    print(f"{person.title()}'s second favorite number is {nums['num2']}")
    print(f"{person.title()}'s third favorite number is {nums['num3']}")

