from os import walk
from importlib import import_module
from apps.module.models import Module, ModuleType
from django.db.models import Q


analyzers = {}

for path, _, files in walk('siteq/pages/analyze/plugins'):
    if '__pycache__' in path:
        continue
    for file in files:
        if file in ['base.py', 'load.py']:
            continue
        module = import_module(f'siteq.pages.analyze.plugins.{file[:-3]}')
        module = getattr(module, file[:-3].title()+'Analyzer')
        analyzers[file[:-3]] = module()


print('------------')
print(analyzers, flush=True)
print('------------')

modules = [f.module.pk for f in analyzers.values()]
Module.objects.filter(~Q(pk__in=modules), type=ModuleType.ANALYZER).delete()
