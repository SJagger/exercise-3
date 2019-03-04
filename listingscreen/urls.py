from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='listingscreen-home'),
    path('books/', views.books, name='listingscreen-books'),
    path('add_book/', views.add_book, name='add_book'),
    path('search_book/', views.search_book, name='search_book'),
    path('create_book/', views.create_book, name='create_book'),
    path('edit_book/<id>/', views.edit_book, name='edit_book'),
    path('update_book/<id>/', views.update_book, name='update_book'),
    path('delete_book/<id>/', views.delete_book, name='delete_book'),
    path('movies/', views.movies, name='listingscreen-movies'),
    path('add_movie/', views.add_movie, name='add_movie'),
    path('search_movie/', views.search_movie, name='search_movie'),
    path('create_movie/', views.create_movie, name='create_movie'),
    path('edit_movie/<id>/', views.edit_movie, name='edit_movie'),
    path('update_movie/<id>/', views.update_movie, name='update_movie'),
    path('delete_movie/<id>/', views.delete_movie, name='delete_movie'),
    path('tvshows/', views.tvshows, name='listingscreen-tvshows'),
    path('add_tvshow/', views.add_tvshow, name='add_tvshow'),
    path('search_tvshow/', views.search_tvshow, name='search_tvshow'),
    path('create_tvshow/', views.create_tvshow, name='create_tvshow'),
    path('edit_tvshow/<id>/', views.edit_tvshow, name='edit_tvshow'),
    path('update_tvshow/<id>/', views.update_tvshow, name='update_tvshow'),
    path('delete_tvshow/<id>/', views.delete_tvshow, name='delete_tvshow'),
]
