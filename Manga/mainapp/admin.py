from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Manga)
admin.site.register(MangaChapter)
admin.site.register(MangaChapterPage)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Tag)