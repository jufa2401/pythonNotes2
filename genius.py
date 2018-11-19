import lyricsgenius as genius
api = genius.Genius('J7SX419b2gYDrWYRYmI78IoZ9qUUVPjXPJhubOJ3yXScw7BxGqicsT1mjksrbw8s')

model = api.search_song('Model', 'Gulddreng')
print(model.lyrics)
# gilli = api.search_song('Su Casa', 'Gilli')
molo = api.search_song('Skejsen', 'MOLO')
print(molo.lyrics)

# print(gilli.lyrics)



# artist = api.search_artist('Drake', max_songs=3)
# song = api.search_song('Marvin\'s room',artist.name)


# api.search_song('Drunk in the morning', 'Lukas Graham').save_lyrics()
# api.search_song('Ked af Det', 'Gulddreng').save_lyrics()



# artist.save_lyrics()