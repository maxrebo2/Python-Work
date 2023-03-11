def make_album(artist, title, tracks=0):

	album_dict = {'artist': artist.title(), 'title': title.title(),}
	if tracks:
		album_dict['tracks'] = tracks
	return album_dict

album = make_album('Green Day', 'Dookie')
print(album)

album = make_album('Pink Floyd', 'Dark Side of The Moon')
print(album)

album = make_album('Simon and Garfunkel', 'Sounds of Silence', tracks=11)
print(album)

