from django.urls import path
from apps.repository.views import Repository

app_name = 'repository'
urlpatterns = [
    path('', Repository.as_view(), name='index')

]