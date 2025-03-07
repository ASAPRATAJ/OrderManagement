# Generated by Django 4.2.15 on 2025-02-12 20:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="company_address",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="customuser",
            name="invoice_name",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="customuser",
            name="nip",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name="customuser",
            name="phone_number",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
