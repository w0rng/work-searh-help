from uuid import uuid4
from django.db import models
from django.utils.translation import ugettext_lazy as _
from typing import Type


class UUIDModel(models.Model):
    id = models.UUIDField(_("ID"), default=uuid4, primary_key=True, editable=False)

    class Meta:
        abstract = True


class CreatedModel(models.Model):
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)

    class Meta:
        abstract = True


def enum_max_length(text_choices: Type[models.Choices]) -> int:
    return max(len(value) for value in text_choices.values)  # noqa: WPS110
