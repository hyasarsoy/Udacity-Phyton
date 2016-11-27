import webbrowser #import browser

#define to class class inculude the movie detail, 
class Movie (): #class is start
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube): #define the movie information
        self.title = movie_title #Movie title
        self.storyline = movie_storyline #Story line
        self.poster_image_url = poster_image #İmage 
        self.trailer_youtube_url = trailer_youtube #trailer video
