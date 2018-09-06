from django.contrib import admin
from apps.devs.models import Company, Software, Developer


class DeveloperAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastname', 'email')
    search_fields = ('name', 'email')


admin.site.register(Company)
admin.site.register(Software)
admin.site.register(Developer, DeveloperAdmin)
