from django.conf.urls.defaults import *

from ootd.rhythms.views import rhythm


urlpatterns = patterns(' ',
    (r'^$', rhythm),
)
