from django.db import models

# Create your models here.
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Source(models.Model):
    title = models.CharField(max_length=250, default=None, null=True, blank=True)
    title_specific = models.CharField(default=None, null=True, blank=True, max_length=250)
    content = models.CharField(max_length=250)
    content_specific = models.CharField(default=None, null=True, blank=True, max_length=250)
    base_url = models.CharField(default=None, null=True, blank=True, max_length=250)
    url = models.CharField(max_length=250)
    details_url = models.CharField(max_length=250, default=None, null=True, blank=True)
    author = models.CharField(max_length=250)
    img = models.CharField(max_length=250, default=None, null=True, blank=True)
    delete_tags = models.CharField(max_length=250, default=None, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Источник'
        verbose_name_plural = 'Источники'

    def __str__(self):
        return self.author


class News(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    url = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    img = models.CharField(max_length=250, default=None, null=True, blank=True)
    published = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title
