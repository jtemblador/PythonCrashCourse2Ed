
cities = {
    'Hong Kong' : {
        'country' : 'china',
        'pop' : 7.3,
        'currency' : 'Yen',
    },
    'Amsterdam' : {
        'country' : 'netherlands',
        'pop' : 0.8,
        'currency' : 'Euro',
    },
    'Lagos' : {
        'country' : 'nigeria',
        'pop' : 15.3,
        'currency' : 'Naira',
    }
}

for city, info in cities.items():
    print(f"{city} is a city in {info['country'].title()}.")
    print(f"Population: {info['pop']} million!")
    print(f"{info['currency']} is their currency.\n")

