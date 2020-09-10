from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import News, Category
from .serializers import NewsSerializer


class WorldNewsView(generics.ListAPIView):
    try:
        queryset = News.objects.filter(category=Category.objects.get(name='В мире')).all()
        serializer_class = NewsSerializer
    except: print()

class KyrgyzNewsView(generics.ListAPIView):
    try:
        queryset = News.objects.filter(category=Category.objects.get(name='В Кыргызстане')).all()
        serializer_class = NewsSerializer
    except: print()

class MovieNewsView(generics.ListAPIView):
    try:
        queryset = News.objects.filter(category=Category.objects.get(name='Кино')).all()
        serializer_class = NewsSerializer
    except: print()

class MusicNewsView(generics.ListAPIView):
    try:
        queryset = News.objects.filter(category=Category.objects.get(name='Музыка')).all()
        serializer_class = NewsSerializer
    except: print()

class AutoNewsView(generics.ListAPIView):
    try:
        queryset = News.objects.filter(category=Category.objects.get(name='Авто')).all()
        serializer_class = NewsSerializer
    except: print()

class TechnologyNewsView(generics.ListAPIView):
    try:
        queryset = News.objects.filter(category=Category.objects.get(name='Технологии')).all()
        serializer_class = NewsSerializer
    except: print()

class SportNewsView(generics.ListAPIView):
    try:
        queryset = News.objects.filter(category=Category.objects.get(name='Спорт')).all()
        serializer_class = NewsSerializer
    except: print()