# .keys() for keys
# .values() for value of key 
# .items() for both key and value

fav_langs = {
    'jen' : 'python', 
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}

#Printing Sarah's favorite language
print(f"Sarah's favorite language is {fav_langs['sarah'].title()}")

#Printing everyone's name using a for loop
for name, lang in fav_langs.items() :
    print(f"{name.title()}'s favorite language is {lang.title()}.")
    
#Now we'll use .keys() since we just want to use the keys from fav_langs
#Python would start with keys by default <--------
#So "for name in fav_langs :" would provide the same output
for name in fav_langs.keys() :
    print(f"{name.title()}")

#checking to see what our friends' favorite language is!
friends = ['phil', 'sarah']
for name in fav_langs:
    print(name.title())

    if name in friends:
        lang = fav_langs[name].title()
        print(f"\t{name.title()}, I see you like {lang}!")

if 'erin' not in fav_langs.keys():
    print("Erin, please take the poll!")

#sorting a list
for name in sorted(fav_langs.keys()):
    print(f"{name.title()}, thanks for taking the poll!")

#this will print ALL values, even repeated values
for langs in fav_langs.values():
    print(langs.title())

#for all values with NO repeated values, we'll use a set
for langs in set(fav_langs.values()):
    print(langs.title())

