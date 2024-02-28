# Generated by Django 4.2.9 on 2024-02-01 20:10

import django.utils.timezone
from django.db import migrations, models
from django_safemigrate import Safe


class Migration(migrations.Migration):
    safe = Safe.always

    dependencies = [
        ("projects", "0113_disable_analytics_addons"),
    ]

    operations = [
        migrations.AlterField(
            model_name="domain",
            name="skip_validation",
            field=models.BooleanField(
                default=False, verbose_name="Skip validation process."
            ),
        ),
        migrations.AlterField(
            model_name="domain",
            name="validation_process_start",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="Start date of the validation process.",
            ),
            preserve_default=False,
        ),
    ]