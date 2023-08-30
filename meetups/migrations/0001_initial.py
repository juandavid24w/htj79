# Generated by Django 4.2.4 on 2023-08-30 13:05

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('glug', '0001_initial'),
        ('hacktivist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meetups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('platform', models.CharField(choices=[('Online', 'Online'), ('Offine', 'Offline')])),
                ('venue', models.TextField()),
                ('description', models.TextField()),
                ('minutes', models.FileField(upload_to='meetups/minutes/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])])),
                ('poster', models.ImageField(upload_to='meetups/poster/', verbose_name='Poster')),
                ('glug', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='glug.glug')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hacktivist.locations')),
            ],
        ),
    ]
