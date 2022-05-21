from multiprocessing.pool import ThreadPool
from typing import List

import requests
from api.v1.resume.serializers import ResumeSerializer
from api.v1.vacancy.serializers import VacancySerializer
from apps.module.models import ConfigModule, Module, ModuleType
from apps.resume.models import Resume
from apps.user.models import User
from apps.vacancy.models import Vacancy
from connectors.serializers import FilterSerializer
from django.core.cache import cache
from django.db.models import Q


class FilterVacancies:
    Model = Vacancy

    def __init__(self, user: User):
        self.user = user

    def _get_filter_modules(self) -> List[Module]:
        return Module.objects.filter(
            pk__in=ConfigModule.objects.filter(user=self.user, enabled=True)
            .values_list("module", flat=True)
            .filter(module__type=ModuleType.FILTER)
            .filter(Q(module__role__isnull=True) | Q(module__role=self.user.role))
        )

    def _get_vacancies(self):
        return self.Model.objects.filter(
            Q(source__id__in=ConfigModule.objects.filter(user=self.user, enabled=True).values_list("module", flat=True))
            | Q(source__isnull=True)
        )

    def _get_resume(self):
        return self.user.get_resume()

    def _send_data(self, module: Module):
        url = module.endpoint
        vacancies = self._get_vacancies()
        data = {
            "vacancies": VacancySerializer(vacancies, many=True).data,
            "resume": ResumeSerializer(self._get_resume()).data,
        }
        scores = FilterSerializer(requests.post(url, json=data).json(), many=True).data
        for score in scores:
            score["vacancy"] = vacancies.get(pk=score["id"])
        return scores

    def _get_response_from_module(self):
        with ThreadPool(self.user.subscriber.subscription.level + 1) as pool:
            return pool.map(self._send_data, self._get_filter_modules())

    def filter(self):
        if user_cache := cache.get(self.user.id):
            return user_cache
        scores = self._get_response_from_module()
        total = {}
        for filter in scores:
            for data in filter:
                total[data["vacancy"]] = total.get(data["vacancy"], 0) + data["score"]
        result = sorted(total, key=lambda x: total[x], reverse=True)
        if not result:
            result = self.Model.objects.all().order_by("?")
        cache.set(self.user.id, result, timeout=60 * 60 * 24)
        return result


class FilterResumes(FilterVacancies):
    Model = Resume

    def _get_resumes(self):
        return Resume.objects.filter(
            Q(source__id__in=ConfigModule.objects.filter(user=self.user, enabled=True).values_list("module", flat=True))
            | Q(source__isnull=True)
        )

    def _get_my_vacancies(self):
        return Vacancy.objects.filter(user=self.user)

    def _send_data(self, module: Module):
        url = module.endpoint
        resumes = self._get_resumes()
        scores = {}
        for vacancy in self._get_my_vacancies():
            data = {
                "vacancies": ResumeSerializer(resumes, many=True).data,
                "resume": VacancySerializer(vacancy).data,
            }
            tmp_scores = FilterSerializer(requests.post(url, json=data).json(), many=True).data
            for score in tmp_scores:
                scores[score["id"]] = scores.get(score["id"], 0) + score["score"]
        result = []
        for pk in scores:
            result.append({"vacancy": resumes.get(pk=pk), "score": scores[pk]})
        return result
