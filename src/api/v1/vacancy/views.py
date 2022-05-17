from api.v1.vacancy.serializers import VacancySerializer
from apps.vacancy.models import Vacancy
from rest_framework.viewsets import GenericViewSet, mixins


class VacancyViewSet(GenericViewSet, mixins.CreateModelMixin):
    serializer_class = VacancySerializer
