from rest_framework import serializers
from .models import News, Poll

class PollsSerializer(serializers.ModelSerializer):
    choices = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Poll
        fields = '__all__'
        depth = 1


class NewsSerializer(serializers.ModelSerializer):

    poll = PollsSerializer(many=True)

    class Meta:
        model = News
        fields = '__all__'
        depth = 1
