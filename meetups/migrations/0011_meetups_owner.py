# Generated by Django 4.2.6 on 2023-10-18 18:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("meetups", "0010_meetups_minutes"),
    ]

    operations = []