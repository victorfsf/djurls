
from djurls import uconf
from tests.mock import urls
from tests.mock import views
from tests.utils import check_url
import pytest


def test_create_uconf():
    fn_based = uconf(namespace='mock')
    fn_based('^fn-based/', name='fn-based')(views.fn_based_view)
    assert check_url('fn-based', urls.mock_patterns) is True


def test_uconf_raises_type_errors():

    with pytest.raises(TypeError):
        uconf(namespace='errors', include='errors_patterns')

    with pytest.raises(TypeError):
        uconf(invalid_argument='errors')
