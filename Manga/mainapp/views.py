from django.shortcuts import render
from .models import Manga, MangaChapter

# Create your views here.
def index(request):
    chapters = MangaChapter.objects.all()
    return render(request, 'index.html', context={'chapters': chapters})
