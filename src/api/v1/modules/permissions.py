from typing import TYPE_CHECKING

from rest_framework.permissions import SAFE_METHODS, BasePermission

if TYPE_CHECKING:
    from apps.module.models import Module


class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj: Module):
        return bool(
            request.method in SAFE_METHODS
            or request.user
            and request.user.is_authenticated
            and obj.author == request.user
        )
