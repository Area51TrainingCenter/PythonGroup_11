# Generated by Django 2.1 on 2018-09-23 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='repositories',
            name='avatar_url',
            field=models.URLField(default=None),
        ),
    ]
