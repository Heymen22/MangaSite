from django.db import models

# Create your models here.
class Manga(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название манги')
    description = models.TextField(max_length=1000, verbose_name='Описание манги')
    author = models.ForeignKey('Author', verbose_name='Автор манги', on_delete=models.SET_NULL(), null=True)
    archive = models.FileField(upload_to='manga/', verbose_name='Архив с мангой')
    preview = models.ImageField(verbose_name='Превью манги')
    genres = models.ManyToManyField('Genre', verbose_name='Жанры манги')
    tags = models.ManyToManyField('Tag', verbose_name='Тэги манги')
    raiting = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='Рейтинг манги', default=0, editable=False)

