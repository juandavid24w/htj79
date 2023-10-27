# Generated by Django 4.2.6 on 2023-10-18 18:09

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("meetups", "0009_remove_meetups_minutes"),
    ]

    operations = [
        migrations.AddField(
            model_name="meetups",
            name="minutes",
            field=models.FileField(
                default=django.utils.timezone.now,
                upload_to="",
                validators=[django.core.validators.FileExtensionValidator(["pdf"])],
            ),
            preserve_default=False,
        ),
    ]