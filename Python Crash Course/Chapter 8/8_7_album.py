# 8-7. Album: Write a function called make_album() that builds
# a dictionary describing a music album. The function should
# take in an artist name and an album title, and it should
# return a dictionary containing these two pieces of
# information. Use the function to make three dictionaries
# representing different albums. Print each return value to
# show that the dictionaries are storing the album information
# correctly.

# Use None to add an optional parameter to make_album() that
# allows you to store the number of songs on an album. If the
# calling line includes a value for the number of songs, add
# that value to the album’s dictionary. Make at least one new
# function call that includes the number of songs on an album.

def make_album(name, album, songs=None):
    if songs:
        return { "Artist Name" : name, "Album Title" : album, "Songs" : songs }
    return { "Artist Name" : name, "Album Title" : album }

album_1 = make_album("Queen", "A Night at the Opera")
album_2 = make_album("Billy Joel", "Piano Man")
album_3 = make_album("The Eagles", "Hotel California", 9)

for album in [album_1, album_2, album_3]:
    if album.get("Songs", 0) > 0:
        print(f"{album["Album Title"]} was released by {album["Artist Name"]} and has {album['Songs']} songs.")
    else:
        print(f"{album["Album Title"]} was released by {album["Artist Name"]}.")
