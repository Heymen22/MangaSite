from django.contrib import admin
from .models import *

# Register your models here.
class MangaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Manga, MangaAdmin)
admin.site.register(MangaChapter)
admin.site.register(MangaChapterPage)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Tag)