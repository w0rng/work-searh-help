from apps.resume.models import Tag
from apps.vacancy.models import Vacancy
import requests
import re

class Loader:
    URL = 'https://api.hh.ru/vacancies'

    @classmethod
    def load(cls, resume):
        tags = ' '.join(resume.tags.all().values_list('name', flat=True))
        url = f'{cls.URL}?text={tags}&salary={int(resume.price)}'
        data = requests.get(url).json()
        print(data, flush=True)
        for vacancy in data.get('items', []):
            tags = re.findall('[a-zA-Z]{2,}', vacancy['snippet']['requirement'] + ' ' + vacancy['name'])
            tags = [t.lower() for t in tags if t != 'highlighttext']
            tags = [Tag.objects.get_or_create(name=t)[0] for t in tags]

            vac = Vacancy.objects.get_or_create(
                name=vacancy['name'],
                price=vacancy['salary']['from'] if vacancy['salary'] and vacancy['salary']['from'] else 0,
                description=vacancy['snippet']['requirement']
            )[0]
            vac.tags.set(tags)
            vac.save()
