from rest_framework import serializers


class VacancyFilterSerializer(serializers.ModelSerializer):
    pk = serializers.UUIDField(required=True)
    score = serializers.FloatField(required=True)
