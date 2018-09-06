from django.conf.urls import url
from apps.devs import views


urlpatterns = [
    url(r'^create-dev/$', views.create_dev),
    url(r'^dev-create/$', views.CreateDevView.as_view()),
    url(r'^thanks/$', views.thanks),
]

