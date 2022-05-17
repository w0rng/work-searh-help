from typing import TYPE_CHECKING

from api.v1.modules.permissions import IsAuthorOrReadOnly
from api.v1.modules.serializers import ConfigSerializer, ModuleSerializer
from apps.module.models import ConfigModule, Module
from django.db.models import Q
from drf_yasg.utils import no_body, swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

if TYPE_CHECKING:
    from apps.user.models import User


class ModuleViewSet(ModelViewSet):
    serializer_class = ModuleSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def get_queryset(self):
        user: User = self.request.user
        if not user or not user.is_authenticated:
            return Module.objects.none()
        if user.subscriber.subscription.level == 0:
            return Module.objects.none()
        if user.subscriber.subscription.level == 1:
            return Module.objects.filter(author=user)
        return Module.objects.filter(Q(author=user) | Q(public=True))

    def perform_create(self, serializer):
        user: User = self.request.user
        if not user or not user.is_authenticated:
            return
        if user.subscriber.subscription.level == 0:
            return
        if user.subscriber.subscription.level == 1:
            serializer.save(author=user, public=True)
        serializer.save(author=user)

    def perform_update(self, serializer):
        user: User = self.request.user
        if not user or not user.is_authenticated:
            return
        serializer.save(author=user)

    @swagger_auto_schema(request_body=no_body, responses={200: ConfigSerializer()})
    @action(detail=True, methods=["post"])
    def connect(self):
        module = self.get_object()
        user = self.request.user
        if not user or not user.is_authenticated:
            return
        if user.subscriber.subscription.level == 0:
            return
        if user.subscriber.subscription.level == 1:
            if module.author != user:
                return
        config = ConfigModule.objects.create(module=module, user=user, enabled=True)
        serializer = ConfigSerializer(config)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=no_body, responses={200: ConfigSerializer()})
    @action(detail=True, methods=["post"])
    def disable(self):
        module = self.get_object()
        user = self.request.user
        config = get_object_or_404(ConfigModule, module=module, user=user, enabled=True)
        config.enabled = False
        config.save()
        serializer = ConfigSerializer(config)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=no_body, responses={200: ConfigSerializer()})
    @action(detail=True, methods=["post"])
    def enable(self):
        module = self.get_object()
        user = self.request.user
        config = get_object_or_404(ConfigModule, module=module, user=user, enabled=False)
        config.enabled = True
        config.save()
        serializer = ConfigSerializer(config)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=no_body, responses={204: "disable"})
    @action(detail=True, methods=["post"])
    def disconnect(self):
        module = self.get_object()
        user = self.request.user
        config = get_object_or_404(ConfigModule, module=module, user=user, enabled=True)
        config.delete()
        return Response("disable", status=204)
