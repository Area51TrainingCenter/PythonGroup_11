from django.conf.urls import url
from apps.testapp.views import hello
from apps.testapp.views import root
from apps.testapp.views import current_time
from apps.testapp.views import time_ahead

urlpatterns = [
    url(r'^$', root),
    url(r'^hello/$', hello),
    url(r'^time/$', current_time),
    url(r'^time/(\d{1,2})/$', time_ahead)
]
