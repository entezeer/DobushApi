from django.urls import path

from .views import WorldNewsView, KyrgyzNewsView, SportNewsView, TechnologyNewsView, MovieNewsView, MusicNewsView, \
    AutoNewsView, ForeignNewsView

urlpatterns = (
    path('world_news', WorldNewsView.as_view()),
    path('kg_news', KyrgyzNewsView.as_view()),
    path('sport_news', SportNewsView.as_view()),
    path('tech_news', TechnologyNewsView.as_view()),
    path('movie_news', MovieNewsView.as_view()),
    path('music_news', MusicNewsView.as_view()),
    path('auto_news', AutoNewsView.as_view()),
    path('foreign_news', ForeignNewsView.as_view())
)