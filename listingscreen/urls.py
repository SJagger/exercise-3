from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='listingscreen-home'),
    path('books/', views.books, name='listingscreen-books'),
    path('movies/', views.movies, name='listingscreen-movies'),
    path('tvshows/', views.tvshows, name='listingscreen-tvshows'),
]
