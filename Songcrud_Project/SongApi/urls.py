from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    path('ArtisteList/', views.getArtisteData),
    path('SongList/', views.getSongData),
    path(r'^api/Music_app/(?P<id>[0-9]+)$', views.Song_detail),
]