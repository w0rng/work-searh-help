from apps.resume.models import Tag
from apps.vacancy.models import Vacancy
from rest_framework import serializers


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class VacancySerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Vacancy
        fields = "__all__"
