from django.contrib.auth.models import User
from rest_framework import permissions, viewsets, renderers
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse

import mainapp.permissions
from .serializers import MangaSerializer, UserSerializer, AuthorSerializer, TagSerializer, GenreSerializer, \
    MangaChapterSerializer, MangaChapterPageSerializer
from mainapp.models import Manga, Author, Tag, Genre, MangaChapter, MangaChapterPage


#
#
# @csrf_exempt
# def manga_list(request, format=None):
#     """
#     List all mangas on site or create new manga
#     :param request:
#     :return:
#     """
#     if request.method == 'GET':
#         mangas = Manga.objects.all()
#         serializer = MangaSerializer(mangas, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = MangaSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @csrf_exempt
# def manga_detail(request, pk, format=None):
#     try:
#         manga = Manga.objects.get(pk=pk)
#
#     except Manga.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = MangaSerializer(manga)
#         return JsonResponse(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = MangaSerializer(Manga, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         manga.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)
#

# class MangaList(generics.ListCreateAPIView):
#     """
#     List all manga instances or create new manga instance
#     """
#     queryset = Manga.objects.all()
#     serializer_class = MangaSerializer
#     permission_classes = {
#         permissions.IsAuthenticatedOrReadOnly
#     }
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
#
#
# class MangaDetail(generics.RetrieveUpdateDestroyAPIView):
#     """
#     Retrieve, Update or Delete Manga instance.
#     """
#     queryset = Manga.objects.all()
#     serializer_class = MangaSerializer
#     permission_classes = {
#         permissions.IsAuthenticatedOrReadOnly,
#         mainapp.permissions.IsOwnerOrReadOnly,
#     }
#

class MangaViewSet(viewsets.ModelViewSet):
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        mainapp.permissions.IsOwnerOrReadOnly,
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        mainapp.permissions.IsOwnerOrReadOnly,
    ]


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class GenreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class MangaChapterViewSet(viewsets.ModelViewSet):
    queryset = MangaChapter.objects.all()
    serializer_class = MangaChapterSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        mainapp.permissions.IsMangaOwnerOrReadOnly,
    ]


class MangaChapterPageViewSet(viewsets.ModelViewSet):
    queryset = MangaChapterPage.objects.all()
    serializer_class = MangaChapterPageSerializer
