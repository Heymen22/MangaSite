from rest_framework.generics import ListAPIView

from .serializers import MangaSerializer
from ..models import Manga


class MangaListAPIView(ListAPIView):
    serializer_class = MangaSerializer
    queryset = Manga.objects.all()
