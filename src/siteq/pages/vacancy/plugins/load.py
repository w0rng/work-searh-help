from os import walk
from importlib import import_module
from apps.module.models import Module, ModuleType
from django.db.models import Q


filters = []

for path, _, files in walk('siteq/pages/vacancy/plugins'):
    if '__pycache__' in path:
        continue
    for file in files:
        if file in ['base.py', 'load.py']:
            continue
        module = import_module(f'siteq.pages.vacancy.plugins.{file[:-3]}')
        module = getattr(module, file[:-3].title()+'Filter')
        filters.append(module())


modules = [f.module.pk for f in filter]
Module.objects.filter(~Q(pk__in=modules), type=ModuleType.FILTER).delete()
