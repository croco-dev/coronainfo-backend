from rest_framework import serializers
from .models import Cheer


class CheerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cheer
        exclude = []