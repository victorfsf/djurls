
from django.conf.urls import url
from django.utils.module_loading import import_string


def umap(path, name=None, include=None, namespace=None, urls=None, **kwargs):
    """
        Maps a given URL path and name to a view
        Arguments:
            - path: the URL regex, e.g.: '^teste/(?P<pk>[0-9])/$'.

        Optional arguments:
            - name: the URL name, which Django uses to identify the URL;
            - include: the URL's 'namespace' object name;
            - namespace: the URL's 'namespace';
            - urls: a custom path to the app's urls module, if needed;
            - kwargs: the 'as_view' function kwargs (for class-based views).
    """
    def route_wrapper(view):
        # gets the module name
        module = view.__module__.split('.', 1)[0]
        # gets the view function (checking if it's a class-based view)
        fn = view.as_view(**kwargs) if hasattr(view, 'as_view') else view

        if namespace:
            # imports the urlpatterns object
            base = import_string('{}.{}.urlpatterns'.format(
                module,
                urls if urls else 'urls',
            ))

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
            urlpatterns = import_string('{}.{}.{}'.format(
                module,
                urls if urls else 'urls',
                include if include else 'urlpatterns'
            ))
        # appends the url with its given name
        urlpatterns.append(url(path, fn, name=name))
        return view
    return route_wrapper
