from django.conf.urls import url
from apps.testapp.views import hello
from apps.testapp.views import root
from apps.testapp.views import *


urlpatterns = [
    url(r'^$', root),
    url(r'^hello/$', hello),
    url(r'^time/$', current_time),
    url(r'^time/(\d{1,2})/$', time_ahead),
    url(r'^devs/$', devs),
    url(r'^create-dev/([a-zA-Z]+)/$', create_dev),
    url(r'^devs-template/$', devs_template),
    url(r'^get-dev/(\d{1,2})/$', get_dev),
    url(r'^filter-devs/([a-zA-Z]+)/$', filter_devs),
    url(r'^filter-devs-domain/([a-zA-Z0-9@]+)/$', filter_devs_for_domain),
    url(r'^update-dev/(\d{1,2})/$', update_dev),
    url(r'^delete-dev/(\d{1,2})/$', delete_dev),
    url(r'^create-dev/$', create_dev_improved),
    url(r'^thanks/$', thanks),
]

