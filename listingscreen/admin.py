from django.contrib import admin
from .models import BookList, MovieList, TvShowList
# Register your models here.

admin.site.register(BookList)
admin.site.register(MovieList)
admin.site.register(TvShowList)
