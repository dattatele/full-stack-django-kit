import settings

def i18n(request):
    return {
        'USE_I18N': settings.USE_I18N
    }


def environment(request):
    return {
        'DEBUG': settings.DEBUG
    }

