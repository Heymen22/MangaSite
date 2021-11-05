from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Manga(models.Model):
    owner = models.ForeignKey(User, related_name='manga', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name='Название манги')
    description = models.TextField(max_length=1000, verbose_name='Описание манги')
    slug = models.SlugField(verbose_name='Ссылка', unique=True, db_index=True, max_length=255)
    author = models.ForeignKey('Author', verbose_name='Автор манги', on_delete=models.SET_NULL, null=True)
    preview = models.ImageField(verbose_name='Превью манги')
    genre = models.ManyToManyField('Genre', verbose_name='Жанры манги')
    tag = models.ManyToManyField('Tag', verbose_name='Тэги манги')
    release_date = models.DateField(verbose_name='Дата выхода манги', blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Дата публикации манги на сайте')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.name


class MangaChapter(models.Model):
    class Meta:
        unique_together = ['number', 'manga']

    volume = models.PositiveIntegerField(verbose_name='Номер тома')
    number = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Номер главы')
    author = models.ForeignKey('Author', verbose_name='Автор главы', on_delete=models.SET_NULL, null=True)
    manga = models.ForeignKey('Manga', verbose_name='К какой манге принадлежит глава', related_name='manga_chapters',
                              on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.manga.name} Chapter {self.number}'

    def save(self, *args, **kwargs):
        self.manga.save()
        super().save(*args, **kwargs)


class MangaChapterPage(models.Model):
    class Meta:
        unique_together = ['number', 'chapter']

    number = models.PositiveIntegerField(verbose_name='Номер страницы')
    chapter = models.ForeignKey('MangaChapter', verbose_name='К какой главе принадлежит страница',
                                on_delete=models.CASCADE, related_name='chapter_pages')
    page_image = models.ImageField(verbose_name='Страница')

    def __str__(self):
        return f'{self.chapter.manga.name} Chapter {self.chapter.number} Page {self.number}'


class Author(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='Имя автора')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия автора')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Genre(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название жанра')

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название тэга')

    def __str__(self):
        return self.name


class UserMangaRelation(models.Model):
    RATE_CHOICES = (
        (1, 'Ужасно'),
        (2, 'Плохо'),
        (3, 'Нормально'),
        (4, 'Олично'),
        (5, 'Превосходно'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE, verbose_name='Манга')
    is_liked = models.BooleanField(default=False, verbose_name='Лайк')
    is_favorite = models.BooleanField(default=False, verbose_name='Избранное')
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES, verbose_name='Оценка')
