
from djurls import umap
from tests import urls
from tests import views
import pytest


def check_url(name, patterns=None):
    return len([
        x for x in (patterns if patterns else urls.urlpatterns)
        if getattr(x, 'name', None) == name]) == 1


def test_fn_based_view_url_created():
    assert check_url('fn-based') is True


def test_class_based_view_url_created():
    assert check_url('class-based') is True


def test_view_url_not_exists():
    assert check_url('not-exists') is False


def test_namespace():
    assert check_url('namespaced', urls.mock_patterns) is True


def test_include():
    assert check_url('included', urls.included_patterns) is True


def test_raise_value_error():
    with pytest.raises(ValueError):
        umap('^value-error/', namespace='errors')(views.fn_based_view)


def test_raise_type_error():
    with pytest.raises(TypeError):
        umap(
            '^value-error/',
            namespace='errors',
            include='errors_patterns'
        )(views.fn_based_view)
