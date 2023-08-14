# Generated by Django 4.2.2 on 2023-06-14 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0001_initial'),
        ('member', '0006_alter_members_glug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='institute',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='institutions.institutions', verbose_name='Institution'),
        ),
    ]