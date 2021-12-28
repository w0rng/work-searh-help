from siteq.pages.analyze.plugins.load import analyzers


def load_nav_obj(request):
    return {
            'analyzers': [(k, i) for k, i in analyzers.items()],
        }
