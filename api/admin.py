from django.contrib import admin

# Register your models here.
from .models import Category, Source, News, Poll, Choice

admin.site.register(Category)
admin.site.register(Source)
admin.site.register(News)
admin.site.register(Poll)
admin.site.register(Choice)