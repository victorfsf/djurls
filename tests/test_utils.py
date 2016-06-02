
from djurls.utils import _find_urls_module
from tests.mock import views


def test__find_urls_module_without_views():
    assert _find_urls_module(views.fn_based_view) == 'tests.mock'


def test__find_urls_module_with_views():

    def my_view(request):
        return request

    assert _find_urls_module(my_view) == 'tests'
