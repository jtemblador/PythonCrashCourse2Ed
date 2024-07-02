def make_album(artist, album, songs=None):
    info = {'name': artist, 'album': album.title()}

    if songs:
        info['songs'] = songs
    
    return info

album = make_album('Charli XCX', 'brat', 12)
print(album)

album = make_album('Radiohead', 'The Bends', 13)
print(album)

album = make_album('The Beatles', 'The White Album', 18)
print(album)

