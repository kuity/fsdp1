class Movie:
    """This class describes a movie and contains 3 attributes: title, poster
    image url, and youtube trailer url which have to initialized when a new
    instance of the class is created.
    """

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
