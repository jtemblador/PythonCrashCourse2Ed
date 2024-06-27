pets = ['dog1', 'cat', 'dog2', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

# while loop checks for 'cat' in list 
while 'cat' in pets:
    #removes only first instance of cat 
    pets.remove('cat')
    print(pets)

print(pets)