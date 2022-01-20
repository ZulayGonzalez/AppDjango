from django.contrib import admin
from django.urls import path


def DesdeMovies(self):
    print('===========MOVIES==================')


urlpatterns = [
    path('movies/', DesdeMovies),

]
