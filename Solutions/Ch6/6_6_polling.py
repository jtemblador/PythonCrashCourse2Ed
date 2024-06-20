fav_langs = {
    'jen' : 'python', 
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}

missing_people = [ 'bob', 'phil', 'jane', 'jen']

for name in missing_people:
    if name in fav_langs.keys():
        print(f"Thank you for taking the poll {name}!")
    else:
        print(f"Please take the poll {name}.")
        