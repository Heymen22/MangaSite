from django.contrib.auth.models import User
from rest_framework import serializers

from mainapp.models import Manga, Author, Tag, Genre, MangaChapter, MangaChapterPage


class MangaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Manga
        fields = ['id', 'name', 'description', 'slug', 'preview', 'release_date', 'pub_date', 'updated_date', 'owner',
                  'author', 'genre', 'tag', 'manga_chapters']


class MangaChapterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MangaChapter
        fields = ['id', 'number', 'chapter_pages']


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        # fields = ['id', 'username', 'manga']
        fields = '__all__'
        # depth = 1


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class MangaChapterPageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MangaChapterPage
        fields = '__all__'
