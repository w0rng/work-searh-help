from uuid import uuid4
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from decimal import Decimal



class PriceField(models.DecimalField):
    def __init__(self, verbose_name=None, name=None, max_digits=10,
                 decimal_places=2, **kwargs):
        validators = kwargs.get('validators', [])
        validators.append(MinValueValidator(Decimal('0.0')))
        kwargs['validators'] = validators
        super().__init__(verbose_name, name, max_digits, decimal_places, **kwargs)


class UUIDModel(models.Model):
    id = models.UUIDField(_('ID'), default=uuid4, primary_key=True, editable=False)

    class Meta:
        abstract = True


class CreatedModel(models.Model):
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    class Meta:
        abstract = True
