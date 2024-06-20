
fav_places = {
    'jose' : {
        'p1' : 'alaska',
        'p2' : 'maui',
        'p3' : 'my bed',
    },
    'greg' : {
        'p1' : 'nantucket',
        'p2' : 'cali',
        'p3' : 'russia',
    },
    'bob' : {
        'p1' : 'japan',
        'p2' : 'maine',
        'p3' : 'boston',
    } 
}

for person, places in fav_places.items():
    print(f"{person.title()}'s favorite places are {places['p1'].title()}, {places['p2'].title()}, {places['p3'].title()}!")
    
