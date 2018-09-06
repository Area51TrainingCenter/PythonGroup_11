from django.conf.urls import url
from apps.tests.views import created



urlpatterns = [
    url(r'^buscar/$', created),

]