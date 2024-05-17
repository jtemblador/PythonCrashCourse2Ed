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
#Python would use data even without the .keys() method <--------
#So "for name in fav_langs :" would provide the same output
for name in fav_langs.keys() :
    print(f"{name.title()}")

