from apps.module.models import Module
from rest_framework import serializers


class ModuleSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Module
        fields = "__all__"
