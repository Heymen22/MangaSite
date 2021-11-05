from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import MangaViewSet, UserViewSet, AuthorViewSet, TagViewSet, GenreViewSet, MangaChapterViewSet, \
    MangaChapterPageViewSet

router = DefaultRouter()

router.register('manga', MangaViewSet)
router.register('user', UserViewSet)
router.register('author', AuthorViewSet)
router.register('tag', TagViewSet)
router.register('genre', GenreViewSet)
router.register('manga-chapter', MangaChapterViewSet)
router.register('manga-chapter-page', MangaChapterPageViewSet)

urlpatterns = (
    path('', include(router.urls)),
)
