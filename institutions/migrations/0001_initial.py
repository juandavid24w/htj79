# Generated by Django 4.2.4 on 2023-08-30 13:05

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hacktivist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Institutions',
            fields=[
                ('created_at', models.DateTimeField(auto_created=True, auto_now_add=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=256, verbose_name='Institute Name')),
                ('address', models.TextField(help_text='Address of The Institute', verbose_name='Address')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('location', models.ForeignKey(help_text='Pick your Institute location', on_delete=django.db.models.deletion.RESTRICT, to='hacktivist.locations', verbose_name='Location')),
            ],
            options={
                'verbose_name': 'Institution',
                'verbose_name_plural': 'Institutions',
                'ordering': ['name', '-updated_at'],
            },
        ),
    ]
