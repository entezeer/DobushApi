from rest_framework import serializers
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


class NewsSerializer(serializers.ModelSerializer):
    poll = PollsSerializer()

    class Meta:
        model = News
        fields = '__all__'
        depth = 2
