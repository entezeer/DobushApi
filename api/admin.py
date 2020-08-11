from django.contrib import admin

# Register your models here.
from .models import Category, Source, News

admin.site.register(Category)
admin.site.register(Source)
admin.site.register(News)