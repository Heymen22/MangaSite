from django.shortcuts import render
from .models import Manga

# Create your views here.
def index(request):
    manga = Manga.objects.first()
    return render(request, 'index.html', context={'manga': manga})
