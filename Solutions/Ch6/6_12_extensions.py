
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    'preservatives' : {
        'red 40' : 'does',
        'microplastics' : 'does',
        'corn starch' : 'does not',
    }
}

for key, value in pizza.items():
    if isinstance(value, list):     #Check if value is a list
        print(f"The pizza has {key} that are {', '.join(value)}.")
    elif isinstance(value, dict):   #Check if value is a dictionary
        print(f"With {key} such as {', '.join(value.keys())}.")
        for sub_key, sub_value in value.items():
            print(f"Studies show {sub_key} {sub_value} kill you.")
    else:
        print(f"The pizza has {key} that's {value}.")
