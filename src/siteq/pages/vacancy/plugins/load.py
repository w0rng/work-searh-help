from os import walk
from importlib import import_module

filters = []

for path, _, files in walk('siteq/pages/vacancy/plugins'):
    if '__pycache__' in path:
        continue
    for file in files:
        if file in ['base.py', 'load.py']:
            continue
        module = import_module(f'siteq.pages.vacancy.plugins.{file[:-3]}')
        module = getattr(module, file[:-3].title()+'Filter')
        filters.append(module)
