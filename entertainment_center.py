import media
from fresh_tomatoes import open_movies_page


def main():
    """This is the main function that takes a textfile containing movie 
    information filled in by the user, creates a new Movie class for each
    movie, and calls open_movies_page to generate the webpage for viewing
    the movie information.
    """
    movies = []
    f = open('movie_list.txt', 'r')
    while True:
        title = f.readline()
        pic = f.readline()
        vid = f.readline()
        movies.append(media.Movie(title, pic, vid));

        line = f.readline()
        if not line: 
            break

    open_movies_page(movies)

if __name__ == "__main__":
    main()