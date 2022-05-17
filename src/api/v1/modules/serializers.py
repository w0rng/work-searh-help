from apps.module.models import ConfigModule, Module
from rest_framework import serializers


class ModuleSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Module
        fields = "__all__"


class ConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfigModule
        fields = "__all__"
