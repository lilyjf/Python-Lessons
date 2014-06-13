# titanic, PG-13, 3, 7.7, Drama / Romance
# grease, PG-13, 3, 7.2, Musical / Romance
# the big lebowski, R, 1, 8.2, Comedy / Crime
# jumanji, PG, 3, 6.8, Adventure / Family / Fantasy
# star wars 3, PG-13, 1, 7.7, Action / Adventure / Fantasy

movie_titles = ['Titanic', 'Grease', 'The Big Lebowski', 'Jumanji', 'Star Wars: Episode III']
parental_rating = ['PG-13', 'PG-13', 'R', 'PG', 'PG-13']
bechdel_rating = ['3', '3', '1', '3', '1']
imdb_rating = ['7.7', '7.2', '8.2', '6.8', '7.7']
genre = ['Drama / Romance', 'Musical / Romance', 'Comedy / Crime', 'Adventure / Family / Fantasy', 'Adventure / Fantasy']

for movie_title, parental_rating, bechdel_rating, imdb_rating, genre in zip(movie_titles, parental_rating, bechdel_rating, imdb_rating, genre):
	print "{0}, {1}, {2}, {3}, {4}".format(movie_title, parental_rating, bechdel_rating, imdb_rating, genre)
	
