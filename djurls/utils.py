
from djurls.decorators import umap


def uconf(**kwargs):

    if len(kwargs) != 1:
        raise TypeError(
            'uconf() takes exactly 1 argument. ({} given)'.format(len(kwargs))
        )

    arg_name = list(kwargs.keys()).pop(0)
    if arg_name not in ['include', 'namespace']:
        raise TypeError(
            'Invalid argument: {}'.format(arg_name)
        )

    def uconf_wrapper(path, name=None):
        def url_wrapper(fn):
            return umap(path, name, **kwargs)(fn)
        return url_wrapper
    return uconf_wrapper
