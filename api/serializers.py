from rest_framework import serializers
from .models import News


class NewsSerializer(serializers.ModelSerializer):
    choices = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = News
        fields = '__all__'
        depth = 1
