
from djurls import uconf
from tests import views
from tests.test_decorators import check_url
from tests.urls import mock_patterns
import pytest


def test_raise_type_errors():

    with pytest.raises(TypeError):
        uconf(namespace='errors', include='errors_patterns')

    with pytest.raises(TypeError):
        uconf(invalid_argument='errors')


def test_create_uconf():
    fn_based = uconf(namespace='mock')
    fn_based('^fn-based/', name='fn-based')(views.fn_based_view)
    assert check_url('fn-based', mock_patterns) is True
