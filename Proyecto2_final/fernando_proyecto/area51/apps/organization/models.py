from django.db import models


class Organizations(models.Model):
    login = models.CharField(max_length=50, default=None)
    name = models.CharField(max_length=50, default=None)
    description = models.CharField(max_length=200, default=None)
    avatar_url = models.URLField(default=None)
    blog = models.URLField(default=None)
    email = models.EmailField(default=None)
    public_repos = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.name