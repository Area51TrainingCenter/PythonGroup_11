from django.db import models


class Company(models.Model):
    
    name = models.CharField(
        max_length=50
    )

    address = models.CharField(
        max_length=100
    )

    website = models.URLField()

    country = models.CharField(max_length=30)

    city = models.CharField(max_length=30)


class Developer(models.Model):
    
    name = models.CharField(
        max_length=50
    )

    lastname = models.CharField(
        max_length=50
    )

    email = models.EmailField(
        default=None
    )


class Software(models.Model):
    
    name = models.CharField(
        max_length=50
    )

    version = models.PositiveSmallIntegerField()

    repository = models.URLField(
        max_length=100,
        blank=True,  # Campo VACIO ('')
        null=True  # NULL
    )

    deploy_date = models.DateField()

    company = models.ForeignKey(
        Company,
        default=None,
        on_delete=models.CASCADE
    )

    developer = models.ManyToManyField(
        Developer
    )

