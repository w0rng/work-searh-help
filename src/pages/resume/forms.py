from apps.resume.models import Resume
from django import forms


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        exclude = ["user", "source"]


# Блок про API и способы взаимодействия в теорию
# Как расчитываются баллы
# Картинки кода заменить на листинг
# Где-то в 2.2.3 написать формулу расчетов баллов
# Написать ссылку в руководство пользователя
