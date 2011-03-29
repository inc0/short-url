from django.conf.urls.defaults import *


urlpatterns = patterns('short.views',
    url(r'^$', view="main",),
    url(r'^(?P<suffix>\w+)', view="redirect_to_original",),
)
