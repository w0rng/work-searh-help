from apps.enemy.models import Enemy
from rest_framework import serializers


class FilterSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    score = serializers.IntegerField()
