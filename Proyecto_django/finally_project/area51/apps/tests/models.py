from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Repository(models.Model):
    organization = models.ForeignKey(Organization , on_delete=models.CASCADE,)
    name = models.CharField(max_length=100)
    fecha = models.DateTimeField()
    update = models.DateTimeField(null=True)


    def __str__(self):
        return self.name


