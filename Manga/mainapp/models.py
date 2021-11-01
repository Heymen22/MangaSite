from django.db import models


# Create your models here.
class Manga(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название манги')
    description = models.TextField(max_length=1000, verbose_name='Описание манги')
    author = models.ForeignKey('Author', verbose_name='Автор манги', on_delete=models.SET_NULL, null=True)
    preview = models.ImageField(verbose_name='Превью манги')
    genres = models.ManyToManyField('Genre', verbose_name='Жанры манги')
    tags = models.ManyToManyField('Tag', verbose_name='Тэги манги')
    raiting = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='Рейтинг манги', default=0,
                                  editable=False)

    def __str__(self):
        return self.name


class MangaChapter(models.Model):
    chapter_number = models.DecimalField(max_digits=4, decimal_places=0, verbose_name='Номер главы')
    author = models.ForeignKey('Author', verbose_name='Автор главы', on_delete=models.SET_NULL, null=True)
    manga = models.ForeignKey('Manga', verbose_name='К какой манге принадлежит глава', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.manga.name} Chapter {self.chapter_number}'


class MangaChapterPage(models.Model):
    page_number = models.DecimalField(max_digits=4, decimal_places=0, verbose_name='Номер страницы')
    chapter = models.ForeignKey('MangaChapter', verbose_name='К какой главе принадлежит страница',
                                on_delete=models.CASCADE)
    page_image = models.ImageField(verbose_name='Страница')

    def __str__(self):
        return f'{self.chapter.manga.name} Chapter {self.chapter.chapter_number} Page {self.page_number}'


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
