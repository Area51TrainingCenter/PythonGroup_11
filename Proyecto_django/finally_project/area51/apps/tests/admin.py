from django.contrib import admin
from apps.tests.models import Repository, Organization

admin.site.register(Organization)
admin.site.register(Repository)
