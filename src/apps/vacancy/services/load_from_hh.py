import re

import requests
from apps.resume.models import Tag
from apps.vacancy.models import Vacancy


class Loader:
    URL = "https://api.hh.ru/vacancies"

    @classmethod
    def load(cls, resume):
        tags = list(resume.tags.all())
        tags.sort(key=lambda x: x.vacancies.count(), reverse=True)
        if tags[0].vacancies.count() > 0:
            tags = [t for t in tags if t.vacancies.count() > 0]
        tags = tags[:-5]
        tags = " ".join([t.name for t in tags])
        url = f"{cls.URL}?text={tags}&salary={int(resume.price)}&only_with_salary=True"
        url += "&schedule=remote" if resume.remote else ""
        data = requests.get(url).json()
        for vacancy in data.get("items", []):
            if not vacancy["snippet"]["requirement"]:
                continue
            tags = re.findall("[a-zA-Z]{2,}", vacancy["snippet"]["requirement"] + " " + vacancy["name"])
            tags = [t.lower() for t in tags if t != "highlighttext"]
            tags = [Tag.objects.get_or_create(name=t)[0] for t in tags]

            vac = Vacancy.objects.get_or_create(
                name=vacancy["name"],
                price=vacancy["salary"]["from"] if vacancy["salary"] and vacancy["salary"]["from"] else 0,
                description=vacancy["snippet"]["requirement"],
                city=vacancy["area"]["name"],
                remote=vacancy["schedule"]["id"] == "remote",
            )[0]
            vac.tags.set(tags)
            vac.save()
