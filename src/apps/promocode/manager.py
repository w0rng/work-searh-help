from django.db import models
from hashlib import md5


class PromocodeManager(models.Manager):
    def get(self, *args, **kwargs):
        if 'code' in kwargs:
            kwargs['code'] = md5(kwargs['code'].encode('utf-8')).hexdigest()
        return super().get(*args, **kwargs)
