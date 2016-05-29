
from djurls import umap


class MockViewBase(object):

    @classmethod
    def as_view(cls, **kwargs):
        def fn(request=None):
            return
        return fn


@umap(r'^class-view/$', name='class-based')
class ClassBasedView(MockViewBase):
    pass


@umap(r'^fn-view/$', name='fn-based')
def fn_based_view(request):
    return


@umap(r'^included-view/$', name='included', include='included_patterns')
def included_view(request):
    return


umap(r'^namespaced-view/$', name='namespaced', namespace='mock')(
    ClassBasedView.as_view(template_name='namespace.html')
)
