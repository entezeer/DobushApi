# Create your views here.
from rest_framework import generics
from .models import News, Category, Poll, Choice
from .serializers import NewsSerializer, PollsSerializer, ChoiceSerializer


class WorldNewsView(generics.ListAPIView):
    try:
        queryset = News.objects.filter(category=Category.objects.get(name='В мире')).all()
        serializer_class = NewsSerializer
    except:
        queryset = News.objects.all()
        serializer_class = NewsSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class KyrgyzNewsView(generics.ListAPIView):
    try:
        queryset = News.objects.filter(category=Category.objects.get(name='В Кыргызстане')).all()
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


class PollsView(generics.ListAPIView):
    queryset = Poll.objects.all().order_by('-date')
    serializer_class = PollsSerializer


class PollUpdate(generics.RetrieveUpdateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollsSerializer


class ChoiceUpdate(generics.RetrieveUpdateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
