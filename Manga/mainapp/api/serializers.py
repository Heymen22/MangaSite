from rest_framework import serializers

from ..models import Manga


class MangaSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    slug = serializers.SlugField()

    class Meta:
        model = Manga
        fields = ('id', 'name', 'slug')
