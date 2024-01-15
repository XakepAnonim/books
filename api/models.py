from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    author = models.CharField(max_length=100, verbose_name='Автор')
    year = models.PositiveIntegerField(verbose_name='Год')
    annotation = models.TextField(verbose_name='Анотации')

    def __str__(self):
        return self.title
