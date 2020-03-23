from random import choice
from tmdbv3api import TMDb, Movie, Genre

tmdb = TMDb()
tmdb.api_key = 'be9603d000eacf54e7993c25318325d4'
movie = Movie()
genre = Genre(tmdb.api_key)

def get_details(id):

    movie_details = movie.details(id)
    number_of_genres = len(movie_details.genres)

    if number_of_genres >= 1:
        for genre_index in range(0, number_of_genres):
            while number_of_genres:
                result = movie_details.genres[genre_index]['name']

                if number_of_genres:
                    break
        return result

def search_movie(query):

    result = movie.search(query)
    number_of_movies = len(result)

    if number_of_movies == 0:
        return number_of_movies
    else:
        for res in result:
            random_movie_title = choice(result).title
            
            if res.title == random_movie_title:
                if res.overview == "":
                    print('Sorry, no plot available :c')
                else:
                    title = random_movie_title
                    get_details(res.id)
                    return title, res.id, res.release_date, res.overview

                #break

def get_popular():
    popular_movie = movie.popular()
    random_popular = choice(popular_movie)
    get_details(random_popular.id)
    return random_popular, random_popular.id, random_popular.release_date, random_popular.overview

