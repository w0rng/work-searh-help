from django import forms
from apps.resume.models import Resume, Tag
from django.contrib.admin.widgets import FilteredSelectMultiple


class ResumeForm(forms.ModelForm):

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        widget=FilteredSelectMultiple(
            verbose_name='Теги',
            is_stacked=False
        )
    )

    class Meta:
        model = Resume
        exclude = ['user']


# Блок про API и способы взаимодействия в теорию
# Как расчитываются баллы
# Картинки кода заменить на листинг
# Где-то в 2.2.3 написать формулу расчетов баллов
# Написать ссылку в руководство пользователя
