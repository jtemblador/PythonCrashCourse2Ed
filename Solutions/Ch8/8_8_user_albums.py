def make_album(artist, album, songs=None):
    info = {'name': artist, 'album': album.title()}

    if songs:
        info['songs'] = songs
    
    return info

while True:
    print("Enter Albums/Artist/song count.\n(Enter q to quit)")

    name = input("Name of artist: ")
    if name == 'q':
        break

    info = input("Name of album: ")
    if info == 'q':
        break

    songs = input("# of songs: ")
    if songs == 'q':
        break

    album = make_album(name, info, songs)
    print(album)