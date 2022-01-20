from django.contrib import admin
from django.urls import path


def DesdeGenres(self):
    print('===========GENEROS==================')


urlpatterns = [
    path('genres/', DesdeGenres),
]
