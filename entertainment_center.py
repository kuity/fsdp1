import media
from fresh_tomatoes import open_movies_page

def main():

	movies = [];
	f = open('movelist.txt', 'r')
	while True:
		title = f.readline()
		pic = f.readline()
		vid = f.readline()
		movies.append(media.Movie(title, pic, vid));

		line = f.readline()
		if not line: break

	open_movies_page(movies)

if __name__ == "__main__":
	main()