from django.urls import path 
from . import views

urlpatterns = [
    path("",views.song_list,name="song_list"),
    path("<str:song_name>/",views.song_detail,name="song_detail")
]