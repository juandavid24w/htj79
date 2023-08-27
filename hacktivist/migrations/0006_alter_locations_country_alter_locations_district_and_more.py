# Generated by Django 4.2.4 on 2023-08-27 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hacktivist', '0005_alter_locations_country_alter_locations_district_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locations',
            name='country',
            field=models.CharField(default='India', help_text='', max_length=256, verbose_name='country'),
        ),
        migrations.AlterField(
            model_name='locations',
            name='district',
            field=models.CharField(help_text='', max_length=256, verbose_name='district'),
        ),
        migrations.AlterField(
            model_name='locations',
            name='state',
            field=models.CharField(help_text='', max_length=256, verbose_name='state'),
        ),
    ]
