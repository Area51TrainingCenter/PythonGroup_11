from django.urls import path
from apps.organization.views import OrganizationView, InfoView


app_name = 'organization'
urlpatterns = [

    path('', OrganizationView.as_view(), name='index'),
    path('info/<slug:name_login>', InfoView.as_view(), name='info'),

]

