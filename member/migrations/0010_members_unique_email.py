# Generated by Django 4.2.2 on 2023-08-15 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0009_members_profile_status_alter_members_contact_full_and_more'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='members',
            constraint=models.UniqueConstraint(fields=('email',), name='unique email'),
        ),
    ]