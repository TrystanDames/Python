#8-6
def city_country(city_name, country_name):
	"""Return a full name, neatly formatted."""
	cities_name = f"{city_name}, {country_name}"
	return cities_name.title()
area = city_country('pretoria', 'south africa')
area1 = city_country('chicago', 'illinois')
area2 = city_country('boston', 'massachusetts')
print(area)
print(area1)
print(area2)

#8-7
def make_album(artist_name, album_title, number_of_songs = None):
	song = {'artist': artist_name, 'album': album_title, 'songs': number_of_songs}
	return song
	if number_of_songs:
		album = f"{artist_name}, {album_title}, {number_of_songs}"
	else:
		album = f"{artist_name}, {album_title}"

album = make_album('trystan', 'break down', '11')
print(album)
album = make_album('nf', 'hollow', '15')
print(album)
album = make_album('eminem', 'monster', '15')
print(album)

#8-8
def make_album(artist_name, album_title, number_of_songs = None):
	song = {'artist': artist_name.title(), 'album': album_title.title(), 'songs': number_of_songs}
	return song
while True:
	print("\nEnter an artist and album title:")
	print("\nEnter 'done' to exit any time.")

	artist_name = input("Artist Name: ")
	if artist_name == 'done':
		break
	album_title = input("Album Title: ")
	if artist_name == 'done':
		break
	album = make_album(artist_name, album_title)
	print(f"Artist: {artist_name} \nAlbum: {album_title}")
	
