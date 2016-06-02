
from djurls import umap
from tests.mock import urls
from tests.mock import views
from tests.utils import check_url
import pytest


def test_fn_based_view_url_created():
    assert check_url('fn-based') is True


def test_class_based_view_url_created():
    assert check_url('class-based') is True


def test_view_url_not_exists():
    assert check_url('not-exists') is False


def test_umap_namespace():
    assert check_url('namespaced', urls.mock_patterns) is True


def test_umap_include():
    assert check_url('included', urls.included_patterns) is True


def test_raise_value_error():
    with pytest.raises(ValueError):
        umap('^value-error/', namespace='errors')(views.fn_based_view)


def test_umap_raises_type_error():
    with pytest.raises(TypeError):
        umap(
            '^value-error/',
            namespace='errors',
            include='errors_patterns'
        )(views.fn_based_view)
