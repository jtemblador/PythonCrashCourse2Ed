
pets = {
    'fluffy' : {
        'owner' : 'Bob',
        'age' : 24,
        'breed' : 'mutt'
    },
    'scruffy' : {
        'owner' : 'Alice', 
        'age' : 11,
        'breed' : 'dragon'
    },
}

for pet, owners in pets.items():
    print(f"My name is {pet} and my owner is {owners['owner']}!")
    print(f"I'm {owners['age']} years old!") 
    print(f"My owner tells me I'm a {owners['breed']}!")
