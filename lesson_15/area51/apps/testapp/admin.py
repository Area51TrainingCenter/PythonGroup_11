from django.contrib import admin
from apps.testapp.models import Company, Software, Developer

admin.site.register(Company)
admin.site.register(Software)
admin.site.register(Developer)