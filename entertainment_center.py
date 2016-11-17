import fresh_tomatoes
import media

finding_nemo = media.Movie("Finding Nemo",
                        "Toys Come to Life",
                        "https://upload.wikimedia.org/wikipedia/en/2/29/Finding_Nemo.jpg",
                        "https://www.youtube.com/watch?v=SPHfeNgogVs")

school_of_rock = media.Movie("School of Rock",
                        "Toys Come to Life",
                        "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                        "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

hermano = media.Movie("Hermano",
                        "Toys Come to Life",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQwNDEzNzg1N15BMl5BanBnXkFtZTcwMDgwODk1OA@@._V1_SY1000_CR0,0,679,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=B7c3NcKzSRQ")

movies = [finding_nemo, school_of_rock, hermano]
fresh_tomatoes.open_movies_page(movies)
