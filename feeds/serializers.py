from rest_framework import serializers
from .models import Feed


class FeedsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        exclude = []
