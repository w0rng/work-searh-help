from api.v1.resume.serializers import ResumeSerializer
from rest_framework.viewsets import GenericViewSet, mixins


class ResumeViewSet(GenericViewSet, mixins.CreateModelMixin):
    serializer_class = ResumeSerializer

    def get_serializer_context(self):
        return {
            "user": self.request.user,
            **super().get_serializer_context(),
        }
