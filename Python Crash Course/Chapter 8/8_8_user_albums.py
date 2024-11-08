# 8-8. User Albums: Start with your program from Exercise 8-7.
# Write a while loop that allows users to enter an album’s
# artist and title. Once you have that information, call
# make_album() with the user’s input and print the dictionary
# that’s created. Be sure to include a quit value in the
# while loop.

def make_album(name, album, songs=None):
    if songs:
        return { "Artist Name" : name, "Album Title" : album, "Songs" : songs }
    return { "Artist Name" : name, "Album Title" : album }

active = True
albums = []

while active:
    print("(Enter 'q' at any time to quit)")
    name = input("What is the name of the artist? ")
    print()
    if name == 'q':
        break

    album = input("What album did they make? ")
    print()
    if album == 'q':
        break

    songs = input("How much songs does the album have?\nEnter 0 if you don't know. ")
    print()
    if songs == 'q':
        break
    elif int(songs) == 0:
        songs = None
    else:
        songs = int(songs)
    
    albums.append(make_album(name, album, songs))
    
for album in albums:
    if album.get("Songs", 0) > 0:
        print(f"{album["Album Title"]} was released by {album["Artist Name"]} and has {album['Songs']} songs.")
    else:
        print(f"{album["Album Title"]} was released by {album["Artist Name"]}.")