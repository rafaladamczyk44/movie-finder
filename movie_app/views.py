from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from .forms import SearchForm
from .models import FoundMovie
from .movie_finder_app import search_movie, get_popular
# Create your views here.

def index(req):
    form = SearchForm()
    return render(req, 'movie_app/index.html', {'form': form})

def result(req):
    search_result = req.GET.get('search')
    movie_genre = req.GET.get('movie_genre')
    

    form = SearchForm()
    
    if search_result != '' and  movie_genre == 'none':
        #TYLKO TYTUŁ
        result = search_movie(search_result)

        if result == None:
            result2 = search_movie(search_result)
            movie_title = result2[0]
            movie_id = result2[1]
            movie_release_date = result2[2]
            movie_overview = result2[3]

            return render(req, 'movie_app/result.html', {
                'movie_title': movie_title,
                'movie_id': movie_id,
                'movie_release_date': movie_release_date,
                'movie_overview': movie_overview,
            }) 

        else:
            movie_title = result[0]
            movie_id = result[1]
            movie_release_date = result[2]
            movie_overview = result[3]

            return render(req, 'movie_app/result.html', {
            'movie_title': movie_title,
            'movie_id': movie_id,
            'movie_release_date': movie_release_date,
            'movie_overview': movie_overview,
            })

    elif search_result == '' and movie_genre != 'none':
        #POPULAR
        result = get_popular()
        
        movie_title = result[0]
        movie_id = result[1]
        movie_release_date = result[2]
        movie_overview = result[3]

        return render(req, 'movie_app/result.html', {
            'movie_title': movie_title,
            'movie_id': movie_id,
            'movie_release_date': movie_release_date,
            'movie_overview': movie_overview,
            })
    elif search_result == '' and movie_genre == 'none':
        warning_input = 'Please use one of the forms'
        return render(req, 'movie_app/index.html', {'form':form, 'warning': warning_input})
    else:
        warning_input = 'Please use (only) one of the forms'
        return render(req, 'movie_app/index.html', {'form':form, 'warning': warning_input})
        