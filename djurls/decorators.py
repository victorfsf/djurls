
from django.conf.urls import url
from django.utils.module_loading import import_string
from djurls.utils import _find_urls_module
from functools import partial


def umap(path, name=None, include=None, namespace=None, priority=None):
    """
        Maps a given URL path, name and namespace to a view.
        Arguments:
            - path: the URL regex, e.g.: '^teste/(?P<pk>[0-9])/$'.

        Optional arguments:
            - name: the URL name, which Django uses to identify the URL;
            - include: A custom URL list, previously
                       set on the module's urls.py;
            - namespace: the URL's namespace;
            - priority: the URL's priority;
    """
    def url_wrapper(view):
        # gets the module name
        module = _find_urls_module(view)
        # gets the view function (checking if it's a class-based view)
        fn = view.as_view() if hasattr(view, 'as_view') else view

        if namespace and include:
            raise TypeError(
                'You can\'t use \'namespace\' and \'include\''
                ' at the same time!'
            )

        if namespace:
            # imports the urlpatterns object
            base = import_string('{}.urls.urlpatterns'.format(module))
            # searchs for the namespace
            urlpatterns_list = [
                x for x in base
                if getattr(x, 'namespace', None) == namespace
            ]
            # if the list length is different than 1,
            # then the namespace is either duplicated or doesn't exist
            if len(urlpatterns_list) != 1:
                raise ValueError(
                    'Namespace \'{}\' not in list.'.format(namespace)
                )
            # if the namespace was found, get its object
            urlpatterns = urlpatterns_list.pop(0).url_patterns
        else:
            # imports the urlpatterns object
            urlpatterns = import_string('{}.urls.{}'.format(
                module,
                include or 'urlpatterns'
            ))
        # appends the url with its given name
        call = (
            urlpatterns.append if priority is None
            else partial(urlpatterns.insert, priority)
        )
        call(url(path, fn, name=name))
        return view
    return url_wrapper
