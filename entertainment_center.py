iimport fresh_tomatoes #import the file, file inside the html code :) 
import media #import the mediapy

#define the Movie
finding_nemo = media.Movie("Finding Nemo", #movie Name
                        "Nemo", #description
                        "https://upload.wikimedia.org/wikipedia/en/2/29/Finding_Nemo.jpg", #image
                        "https://www.youtube.com/watch?v=SPHfeNgogVs") #youtube link


#define the Movie
school_of_rock = media.Movie("School of Rock",
                        "School",
                        "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                        "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

#define the Movie
hermano = media.Movie("Hermano",
                        "Hermanoe",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQwNDEzNzg1N15BMl5BanBnXkFtZTcwMDgwODk1OA@@._V1_SY1000_CR0,0,679,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=B7c3NcKzSRQ")

movies = [finding_nemo, school_of_rock, hermano] #write to all movie
fresh_tomatoes.open_movies_page(movies) #its html page you can check this file

