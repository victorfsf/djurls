
from tests.mock import urls


def check_url(name, patterns=None):
    return len([
        x for x in (patterns if patterns else urls.urlpatterns)
        if getattr(x, 'name', None) == name]) == 1
