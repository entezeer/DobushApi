from rest_framework import serializers
from .models import News, Poll


class PollsSerializer(serializers.ModelSerializer):
    choice = serializers.RelatedField(many=True, read_only=True)

    class Meta:
        model = Poll
        fields = '__all__'
        depth = 3


class NewsSerializer(serializers.ModelSerializer):
    poll = PollsSerializer(read_only=True)

    class Meta:
        model = News
        fields = '__all__'
        depth = 3
