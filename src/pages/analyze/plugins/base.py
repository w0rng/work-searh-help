from apps.module.models import ModuleClass, ModuleType


class BaseAnalyzer(ModuleClass):
    type = ModuleType.ANALYZER
    description = ''
    show = True

    def get_queryset(request):
        pass
