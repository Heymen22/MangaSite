from django.urls import path

from .api_views import MangaListAPIView

urlpatterns = [
    path('manga/', MangaListAPIView.as_view(), name='manga')
]