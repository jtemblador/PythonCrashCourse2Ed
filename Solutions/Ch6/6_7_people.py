people = {
    'john' : {'name' : 'John Lennon',
        'band' : 'The Beatles',
        'age' : '24',
        'city': 'liverpool',
        },
    'brian' : { 'name' : 'Brian Wilson',
        'band' : 'The Beach Boys',
        'age' : 22,
        'city' : 'Hawthorne'
        }
}

#people = [beatles, beachboys]

for person, traits in people.items():
    print(f"His name is {traits['name']}")
    print(f"He was in the band {traits['band']}")
    print(f"He was {traits['age']} years old in 1965.")
    print(f"Their hometown is {traits['city'].title()}.\n")
