# djURLs

[![PyPI version](https://badge.fury.io/py/djurls.svg)](https://badge.fury.io/py/djurls)
[![Build Status](https://travis-ci.org/victorfsf/djurls.svg?branch=master)](https://travis-ci.org/victorfsf/djurls)
[![Coverage Status](https://coveralls.io/repos/github/victorfsf/djurls/badge.svg?branch=master)](https://coveralls.io/github/victorfsf/djurls?branch=master)
[![Code Health](https://landscape.io/github/victorfsf/djurls/master/landscape.svg?style=flat)](https://landscape.io/github/victorfsf/djurls/master)


*Decorator for mapping Django URLs.*
Based on Flask's `route` decorator.

Works with Python versions: **2.7, 3.4, 3.5**.

Django versions: **1.7 or greater**.

## Install

```
$ pip install djurls
```

## Usage

###### This usage guide is based on *Django 1.9*.


File: **project/urls.py**
```python
from django.conf.urls import include
from django.conf.urls import url

urlpatterns = [
    url('^app/', include('app.urls', namespace='app'))
]

```


File: **project/app/urls.py**
```python
# Define an empty 'urlpatterns' list
urlpatterns = []
```


File: **project/app/views.py**
```python
from django.views.generic import View
from djurls import umap


@umap(r'^fn-based/$', name='fn_based')
def fn_based_view(request):
    return


@umap(r'^class-based/$', name='class_based')
class ClassBasedView(View):
    template_name = 'app/index.html'


umap(r'^example/$', name='example')(
    ClassBasedView.as_view(template_name='app/example.html')
)
```

#### Namespaces & includes

###### You can also use namespaces/includes with `@umap`:


File: **project/app/urls.py**
```python
from django.conf.urls import include
from django.conf.urls import url

namespace_patterns = []
included_patterns = []

urlpatterns = [
    url(r'^namespace/$', include(namespace_patterns, namespace='test'),
    url(r'^include/$', include(included_patterns),
]
```


File: **project/app/views.py**
```python
from django.views.generic import View
from djurls import umap


@umap(r'^fn-based/$', name='fn_based', namespace='test')
def fn_based_view(request):
    return


@umap(r'^class-based/$', name='class_based', include='included_patterns')
class ClassBasedView(View):
    pass

```

#### Doing the examples above is the same as doing:

File: **project/app/urls.py**
```python
from app.views import fn_based_view
from app.views import ClassBasedView
from django.conf.urls import include
from django.conf.urls import url

namespace_patterns = [
    url(r'^fn-based/$', fn_based_view, name='fn_based'),
]

included_patterns = [
    url(r'^class-based/$', ClassBasedView.as_view(), name='class_based'),
]

urlpatterns = [
    url(r'^namespace/', include(namespace_patterns, namespace='test'),
    url(r'^include/', include(included_patterns),
    url(r'^example/$', ClassBasedView.as_view(
            template_name='app/example.html'), name='example'),
]

```
