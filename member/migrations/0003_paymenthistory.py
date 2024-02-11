# Generated by Django 5.0.2 on 2024-02-11 19:41

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("member", "0002_alter_proofofpayment_transaction_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="PaymentHistory",
            fields=[
                (
                    "created_at",
                    models.DateTimeField(
                        auto_created=True, auto_now_add=True, null=True
                    ),
                ),
                (
                    "payment_date",
                    models.DateField(auto_created=True, auto_now_add=True),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "member",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "proof_of_payment",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="member.proofofpayment",
                    ),
                ),
            ],
            options={
                "verbose_name": "Payment history",
                "verbose_name_plural": "Payment history",
                "ordering": ["-payment_date", "member"],
            },
        ),
    ]