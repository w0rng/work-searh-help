from apps.enemy.models import Tag
from apps.module.models import Module
from apps.resume.models import Resume
from django.core.exceptions import ObjectDoesNotExist
from django.utils.encoding import smart_text
from rest_framework import serializers


class CreatableSlugRelatedField(serializers.SlugRelatedField):
    def to_internal_value(self, data):
        try:
            return self.get_queryset().get_or_create(**{self.slug_field: data})[0]
        except ObjectDoesNotExist:
            self.fail("does_not_exist", slug_name=self.slug_field, value=smart_text(data))
        except (TypeError, ValueError):
            self.fail("invalid")


class ResumeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    tags = CreatableSlugRelatedField(queryset=Tag.objects.all(), slug_field="name", many=True)
    source = serializers.UUIDField()

    def validate_source(self, attrs):
        user = self.context["user"]
        if not Module.objects.filter(id=attrs).exists():
            raise serializers.ValidationError("Модуль не найден или он пренадлежит не вам")
        if not Module.objects.get(id=attrs, author=user):
            raise serializers.ValidationError("Модуль не найден или он пренадлежит не вам")
        return attrs

    def create(self, validated_data):
        validated_data["source"] = Module.objects.get(id=validated_data["source"])
        validated_data["user"] = self.context["user"]
        return super().create(validated_data)

    class Meta:
        model = Resume
        fields = ("id", "name", "tags", "source", "price", "city", "remote")
