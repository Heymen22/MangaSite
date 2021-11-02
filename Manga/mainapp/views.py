from django.shortcuts import render
from .models import Manga, MangaChapter

# Create your views here.
def index(request):
    last_5_mangas = Manga.objects.all()
    return render(request, 'index.html', context={'last_5_mangas': last_5_mangas})
