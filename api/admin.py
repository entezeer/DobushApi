from django.contrib import admin

# Register your models here.
from .models import Category, Source, News, Poll, Choice

admin.site.register(Category)
admin.site.register(Source)
admin.site.register(News)


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question']})]
    inlines = [ChoiceInLine]


admin.site.register(Poll, QuestionAdmin)
