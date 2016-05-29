# djURLs

*Decorator for mapping Django URLs.*

Works with Python versions: **2.6, 2.7, 3.2, 3.3, 3.5**.

Django versions: **1.7 or greater**.

## Usage

###### This usage guide is based on *Django 1.9*.


File: **project/urls.py**
```python

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

@umap('^fn-based/', name='fn_based')
def fn_based_view(request):
    return
    

@umap('^class-based/', name='class_based')
class ClassBasedView(View):
    template_name = 'app/index.html'


umap('^example/', name='example')(
    ClassBasedView.as_view(template_name='app/example.html')
)
```

#### Namespaces & includes

###### You can also use namespaces/includes with `@umap`:


File: **project/app/urls.py**
```python
from django.conf.urls import url

namespace_patterns = []
included_patterns = []

urlpatterns = [
    url('^namespace/', include(namespace_patterns, namespace='test'),
    url('^include/', include(included_patterns),
]
```


File: **project/app/views.py**
```python
from django.views.generic import View
from djurls import umap

@umap('^fn-based/', name='fn_based', namespace='test')
def fn_based_view(request):
    return
    

@umap('^class-based/', name='class_based', include='included_patterns')
class ClassBasedView(View):
    pass

```

#### Doing the examples above is the same as doing:

File: **project/app/urls.py**
```python

from app.views import fn_based_view
from app.views import ClassBasedView

urlpatterns = [
    url('^fn-based/', fn_based_view, name='fn_based'),
    url('^class-based/', ClassBasedView.as_view(), name='class_based'),
    url('^example/', ClassBasedView.as_view(
            template_name='app/example.html'), name='example'),
]

```
