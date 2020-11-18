from django.db import models

# Create your models here.
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField


class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Poll(models.Model):
    question = models.TextField()
    users = ArrayField(models.CharField(max_length=250, blank=True), default=None, null=True, blank=True, max_length=250)

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

    def __str__(self):
        return self.question


class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='choices')
    answer = models.CharField(max_length=200)
    count = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответа'

    def __str__(self):
        return self.answer


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
    language = models.IntegerField(default=None, null=True, blank=True)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, default=None, null=True, blank=True, related_name='polls')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title
