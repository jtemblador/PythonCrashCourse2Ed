rivers = { 'The United States' : 'mississippi',
           'china' : 'yellow',
           'brazil': 'amazon'}

for country, name in rivers.items():
    print(f"The {name.title()} River runs through {country.title()}.")