from api.v1.vacancy.serializers import VacancySerializer
from rest_framework.viewsets import GenericViewSet, mixins


class VacancyViewSet(GenericViewSet, mixins.CreateModelMixin):
    serializer_class = VacancySerializer

    def get_serializer_context(self):
        return {
            "user": self.request.user,
            **super().get_serializer_context(),
        }
