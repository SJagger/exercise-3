from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import BookList, MovieList, TvShowList

def home(request):
    return render(request, 'listingscreen/home.html', {'title': 'Home'})

def books(request):
    books = BookList.objects.all()
    return render(request, 'listingscreen/book/books.html', {'title': 'Books', 'books':books})

@login_required
def create_book(request):
    print(request.POST)
    title = request.GET['title']
    author = request.GET['author']
    pages = request.GET['pages']
    price = request.GET['price']
    book_details = BookList(title=title, author=author, pages=pages, price=price)
    book_details.save()
    return redirect('/books/')

@login_required
def add_book(request):
    return render(request, 'listingscreen/book/add_book.html')

@login_required
def delete_book(request, id):
    books = BookList.objects.get(pk=id)
    books.delete()
    return redirect('/books/')

@login_required
def edit_book(request, id):
    books = BookList.objects.get(pk=id)
    context = {
        'books' : books
    }
    return render(request, 'listingscreen/book/edit_book.html', context)

@login_required
def update_book(request, id):
    books = BookList.objects.get(pk=id)
    books.title = request.GET['title']
    books.author = request.GET['author']
    books.pages = request.GET['pages']
    books.price = request.GET['price']
    books.save()
    return redirect('/books/')

def movies(request):
    movies = MovieList.objects.all()
    return render(request, 'listingscreen/movie/movies.html', {'title': 'Movies', 'movies':movies})

@login_required
def create_movie(request):
    print(request.POST)
    mtitle = request.GET['mtitle']
    director = request.GET['director']
    rating = request.GET['rating']
    movie_details = MovieList(mtitle=mtitle, director=director, rating=rating)
    movie_details.save()
    return redirect('/movies/')

@login_required
def add_movie(request):
    return render(request, 'listingscreen/movie/add_movie.html')

@login_required
def delete_movie(request, id):
    movies = MovieList.objects.get(pk=id)
    movies.delete()
    return redirect('/movies/')

@login_required
def edit_movie(request, id):
    movies = MovieList.objects.get(pk=id)
    context = {
        'movies' : movies
    }
    return render(request, 'listingscreen/movie/edit_movie.html', context)

@login_required
def update_movie(request, id):
    movies = MovieList.objects.get(pk=id)
    movies.mtitle = request.GET['mtitle']
    movies.director = request.GET['director']
    movies.rating = request.GET['rating']
    movies.save()
    return redirect('/movies/')


def tvshows(request):
    tvshows = TvShowList.objects.all()
    return render(request, 'listingscreen/tvshow/tvshows.html', {'title': 'TV Shows', 'tvshows':tvshows})

@login_required
def create_tvshow(request):
    print(request.POST)
    ttitle = request.GET['ttitle']
    seasons = request.GET['seasons']
    network = request.GET['network']
    episodes = request.GET['episodes']
    tvshow_details = TvShowList(ttitle=ttitle, seasons=seasons, network=network, episodes=episodes)
    tvshow_details.save()
    return redirect('/tvshows/')

@login_required
def add_tvshow(request):
    return render(request, 'listingscreen/tvshow/add_tvshow.html')

@login_required
def delete_tvshow(request, id):
    tvshows = TvShowList.objects.get(pk=id)
    tvshows.delete()
    return redirect('/tvshows/')

@login_required
def edit_tvshow(request, id):
    tvshows = TvShowList.objects.get(pk=id)
    context = {
        'tvshows' : tvshows
    }
    return render(request, 'listingscreen/tvshow/edit_tvshow.html', context)

@login_required
def update_tvshow(request, id):
    tvshows = TvShowList.objects.get(pk=id)
    tvshows.ttitle = request.GET['ttitle']
    tvshows.seasons = request.GET['seasons']
    tvshows.network = request.GET['network']
    tvshows.episodes = request.GET['episodes']
    tvshows.save()
    return redirect('/tvshows/')
