
# empty dictionary
info = {}

# flag for loop 
flag = True

while flag:
    # get info
    user = input("Name? ")
    loc  = input("Dream Vacation? ")

    #adding info
    info[user] = loc

    # print info
    for name, loc in info.items():
            print(f"{name.title()} is going to {loc.title()}")
    
    # continue?
    cont = input("Continue? ")
    if cont == 'no':
        flag = False
    