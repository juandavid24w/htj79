# Generated by Django 4.2.6 on 2023-11-08 06:45

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("meetups", "0002_alter_meetups_slug"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="meetups",
            options={"ordering": ["-date", "-time"]},
        ),
    ]
