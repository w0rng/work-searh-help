from apps.enemy.models import Enemy
from rest_framework import serializers


class FilterSerializer(serializers.Serializer):
    id = serializers.SlugRelatedField(queryset=Enemy.objects.all(), slug_field="pk")
    score = serializers.IntegerField()
