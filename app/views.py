from django.shortcuts import render
from app.models import Song

# Create your views here.

def index_view(request):

    context = {
    "songs": Song.objects.all()
    }
    return render(request, "index.html")

def bio_view(request):

    return render(request, "bio.html")

def song_list_view(request):

    context = {
    "songs": Song.objects.all(),
    }
    return render(request, "song_list.html", context)
