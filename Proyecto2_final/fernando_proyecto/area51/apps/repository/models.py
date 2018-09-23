from django.db import models
from apps.organization.models import Organizations

class Repositories(models.Model):
    name = models.CharField(max_length=100, default=None)
    html_url = models.URLField(default=None)
    description = models.CharField(max_length=500, null=True, default=None)
    language = models.CharField(max_length=20, null=True, default=None)
    stargazers_count = models.PositiveIntegerField(default=0)
    forks_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(default=None)
    updated_at = models.DateTimeField(default=None)
    organization = models.ForeignKey(
        Organizations,
        default=None,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name