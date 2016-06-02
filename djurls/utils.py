
import re


def _find_urls_module(view):
    module = view.__module__

    if re.findall(r'.views$|.views.', module):
        return module.split('.views', 1)[0]

    return module.split('.', 1)[0]
