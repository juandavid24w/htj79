# Generated by Django 4.2.2 on 2023-08-08 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0008_members_is_accept_tc_members_is_news_subscribed_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='profile_status',
            field=models.CharField(choices=[(1, 'Profile Info'), (2, 'Membership'), (3, 'Payment Proof'), (4, 'Proof Confirmation'), (5, 'Success')], default=1, max_length=50, verbose_name='Profile Status'),
        ),
        migrations.AlterField(
            model_name='members',
            name='contact_full',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='members',
            name='is_news_subscribed',
            field=models.BooleanField(default=False, verbose_name='Hacktivist News updates'),
        ),
    ]