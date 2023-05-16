# from django.db import models
#
#
# class Article(models.Model):
#
#     title = models.CharField(max_length=256, verbose_name='Название')
#     text = models.TextField(verbose_name='Текст')
#     published_at = models.DateTimeField(verbose_name='Дата публикации')
#     image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
#
#     class Meta:
#         verbose_name = 'Статья'
#         verbose_name_plural = 'Статьи'
#
#     def __str__(self):
#         return self.title

from django.db import models
from django.core.exceptions import ValidationError


class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    articles = models.ManyToManyField('Article', through='Scope', verbose_name='Статьи')

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')

    tags = models.ManyToManyField('Tag', through='Scope', blank=True, verbose_name='Теги')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Scope(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='scopes')
    is_main = models.BooleanField(default=False)

    def clean(self):
        super().clean()
        count_main_tags = self.tag.scopes.filter(is_main=True).count()
        if self.is_main and count_main_tags == 1 and not self.id:
            raise ValidationError('Может быть только один основной раздел')

