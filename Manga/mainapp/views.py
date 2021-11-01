from django.shortcuts import render
from .models import Manga, MangaChapter

# Create your views here.
def index(request):
    mangas = Manga.objects.all()
    return render(request, 'index.html', context={'mangas': mangas})
