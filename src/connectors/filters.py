from multiprocessing.pool import ThreadPool
from typing import List

import requests
from api.v1.resume.serializers import ResumeSerializer
from api.v1.vacancy.serializers import VacancySerializer
from apps.module.models import ConfigModule, Module, ModuleType
from apps.user.models import User
from apps.vacancy.models import Vacancy
from connectors.serializers import FilterSerializer
from django.db.models import Q


class FilterVacancies:
    def __init__(self, user: User):
        self.user = user

    def _get_filter_modules(self) -> List[Module]:
        return Module.objects.filter(
            pk__in=ConfigModule.objects.filter(user=self.user, enabled=True)
            .values_list("module", flat=True)
            .filter(module__type=ModuleType.FILTER)
        )

    def _get_vacancies(self):
        return Vacancy.objects.filter(
            Q(source__id__in=ConfigModule.objects.filter(user=self.user, enabled=True).values_list("module", flat=True))
            | Q(source__isnull=True)
        )

    def _get_resume(self):
        return self.user.resume

    def _send_data(self, module: Module):
        url = module.endpoint
        vacancies = self._get_vacancies()
        resume = ResumeSerializer(self._get_resume()).data
        data = {
            "vacancies": VacancySerializer(vacancies, many=True).data,
            "resume": resume,
        }
        scores = FilterSerializer(requests.post(url, json=data).json(), many=True).data
        for score in scores:
            score["vacancy"] = vacancies.get(pk=score["pk"])
        return scores

    def _get_response_from_module(self):
        with ThreadPool(self.user.subscriber.subscription.level + 1) as pool:
            return pool.map(self._send_data, self._get_filter_modules())

    def filter(self):
        scores = self._get_response_from_module()
        count = len(scores)
        total = {}
        for filter in scores:
            for data in filter:
                total[data["vacancy"]] = total.get(data["vacancy"], 0) + data["score"] / count
        return sorted(total, key=lambda x: total[x], reverse=True)
