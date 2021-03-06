# Generated by Django 3.0.6 on 2020-05-15 16:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("price_tracker", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product", options={"ordering": ["-created"]},
        ),
        migrations.AddField(
            model_name="productprice",
            name="product",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="product_prices",
                to="price_tracker.Product",
            ),
        ),
    ]
