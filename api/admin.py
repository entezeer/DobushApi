from django.contrib import admin

# Register your models here.
from .models import Category, Source, News, Poll, Choice

admin.site.register(Category)
admin.site.register(Source)
admin.site.register(News)


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question']}),
                 ('users', {'fields': ['users'], 'classes': ['collapse']})]
    inlines = [ChoiceInLine]


admin.site.register(Choice)
admin.site.register(Poll, QuestionAdmin)
