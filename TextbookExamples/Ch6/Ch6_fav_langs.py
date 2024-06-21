
fav_langs = {
    'jen' : ['python', 'ruby'], 
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, langs in fav_langs.items():
    print(f"{name}'s favorite languages are ")
    for lang in langs:
        print(f"\t{lang.title()}")