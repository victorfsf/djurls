
from djurls.decorators import umap
from functools import partial


def uconf(**kwargs):
    """
        Function to set a default namespace/include.
        It returns a decorator with the namespace/include argument already set.
        Arguments:
            - include: A custom URL list, previously
                       set on the module's urls.py;
            - namespace: the URL's namespace.
    """
    if len(kwargs) != 1:
        # this function must have exactly
        # one specific argument (namespace or include)
        raise TypeError(
            'uconf() takes exactly 1 argument. ({} given)'.format(len(kwargs))
        )
    # gets the argument name
    arg_name = list(kwargs.keys()).pop(0)
    # checks if it has a valid name (it must be 'namespace' or 'include')
    if arg_name not in ['include', 'namespace']:
        # if it's not a valid name, raise a TypeError
        raise TypeError(
            'Invalid argument: {}'.format(arg_name)
        )
    # creates the decorator with namespace/include already set.
    return partial(umap, **kwargs)
