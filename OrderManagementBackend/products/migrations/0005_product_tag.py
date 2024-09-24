# Generated by Django 4.2.15 on 2024-09-24 19:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0004_alter_product_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="tag",
            field=models.CharField(
                choices=[
                    ("basic", "Podstawowa"),
                    ("extend", "Rozszerzona"),
                    ("premium", "Premium"),
                    ("weekly_flavors", "Smaki tygodnia"),
                ],
                default="basic",
                max_length=50,
            ),
        ),
    ]
