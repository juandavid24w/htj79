# Generated by Django 4.2.6 on 2023-10-07 20:15

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "hacktivist",
            "0005_alter_locations_country_alter_locations_district_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="locations",
            name="country",
            field=models.CharField(
                default="India", max_length=256, verbose_name="country"
            ),
        ),
        migrations.AlterField(
            model_name="locations",
            name="district",
            field=models.CharField(max_length=256, verbose_name="district"),
        ),
        migrations.AlterField(
            model_name="locations",
            name="location",
            field=django.contrib.gis.db.models.fields.PointField(
                blank=True,
                geography=True,
                help_text="point your Institution/GLUG location",
                null=True,
                srid=4326,
                verbose_name="location",
            ),
        ),
        migrations.AlterField(
            model_name="locations",
            name="state",
            field=models.CharField(max_length=256, verbose_name="state"),
        ),
    ]