from django.shortcuts import render
from django.http import HttpResponse

def song_list(request):
    songs = [
        "Tere Naam",
        "Tum Hi Ho",
        "Saat Samundar",
        "Ghar Se Nikalte Hi"
    ]
    return render(request,"songs/song_list.html",{"songs":songs})

def song_detail(request,song_name):
    return HttpResponse(f'You selected: {song_name}')
