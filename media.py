iimport webbrowser #import browser

#define to class class inculude the movie detail, define the movie information
class Movie ():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube): 
        self.title = movie_title #movie title
        self.storyline = movie_storyline #story line
        self.poster_image_url = poster_image #image 
        self.trailer_youtube_url = trailer_youtube #trailer video
