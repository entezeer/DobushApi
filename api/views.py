from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import News, Category
from .serializers import NewsSerializer


class WorldNewsView(generics.ListAPIView):
    try:
        queryset = News.objects.filter(category=Category.objects.get(name='В мире')).all()
        serializer_class = NewsSerializer
    except:
        queryset = News.objects.all()
        serializer_class = NewsSerializer

class KyrgyzNewsView(generics.ListAPIView):
    try:
        queryset = News.objects.filter(category=Category.objects.filter(name='В Кыргызстане')).all()
        serializer_class = NewsSerializer
    except:
        queryset = News.objects.all()
        serializer_class = NewsSerializer

class MovieNewsView(generics.ListAPIView):
    try:
        queryset = News.objects.filter(category=Category.objects.get(name='Кино')).all()
        serializer_class = NewsSerializer
    except:
        queryset = News.objects.all()
        serializer_class = NewsSerializer

class MusicNewsView(generics.ListAPIView):
    try:
        queryset = News.objects.filter(category=Category.objects.get(name='Музыка')).all()
        serializer_class = NewsSerializer
    except:
        queryset = News.objects.all()
        serializer_class = NewsSerializer

class AutoNewsView(generics.ListAPIView):
    try:
        queryset = News.objects.filter(category=Category.objects.get(name='Авто')).all()
        serializer_class = NewsSerializer
    except:
        queryset = News.objects.all()
        serializer_class = NewsSerializer

class TechnologyNewsView(generics.ListAPIView):
    try:
        queryset = News.objects.filter(category=Category.objects.get(name='Технологии')).all()
        serializer_class = NewsSerializer
    except:
        queryset = News.objects.all()
        serializer_class = NewsSerializer

class SportNewsView(generics.ListAPIView):
    try:
        queryset = News.objects.filter(category=Category.objects.get(name='Спорт')).all()
        serializer_class = NewsSerializer
    except:
        queryset = News.objects.all()
        serializer_class = NewsSerializer

class ForeignNewsView(generics.ListAPIView):
    try:
        queryset = News.objects.filter(category=Category.objects.get(name="Иностранные")).all()
        serializer_class = NewsSerializer
    except:
        queryset = News.objects.all()
        serializer_class = NewsSerializer

class UpdateNewsPoll(generics.RetrieveUpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer