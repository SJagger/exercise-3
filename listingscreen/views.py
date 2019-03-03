from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'listingscreen/home.html', {'title': 'Home'})

def books(request):
    return render(request, 'listingscreen/books.html', {'title': 'Books'})

def movies(request):
    return render(request, 'listingscreen/movies.html', {'title': 'Movies'})

def tvshows(request):
    return render(request, 'listingscreen/tvshows.html', {'title': 'TV Shows'})
