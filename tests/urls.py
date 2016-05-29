
from django.conf.urls import include
from django.conf.urls import url

mock_patterns = []
included_patterns = []

urlpatterns = [
    url('^mock/', include(mock_patterns, namespace='mock')),
    url('^included/', include(included_patterns))
]
