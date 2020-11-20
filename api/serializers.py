from django.http import QueryDict
from rest_framework import serializers, viewsets, parsers
from rest_framework.response import Response
from rest_framework.utils import json

from .models import News, Poll, Choice


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'


class PollsSerializer(serializers.ModelSerializer):
    choice = ChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Poll
        fields = '__all__'
        depth = 2


class NewsSerializer(serializers.ModelSerializer):
    poll = PollsSerializer()

    class Meta:
        model = News
        fields = '__all__'
        depth = 2

