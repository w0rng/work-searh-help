from typing import TYPE_CHECKING

from api.v1.modules.permissions import IsAuthorOrReadOnly
from api.v1.modules.serializers import ModuleSerializer
from apps.module.models import Module
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
        if user.is_superuser:
            return Module.objects.all()
        if user.subscriber.subscription.level == 0:
            return Module.objects.none()
        if user.subscriber.subscription.level == 1:
            return Module.objects.filter(author=user)
        return Module.objects.all()
