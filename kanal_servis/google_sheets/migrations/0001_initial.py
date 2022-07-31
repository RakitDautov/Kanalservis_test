# Generated by Django 2.2.19 on 2022-07-30 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("number", models.IntegerField()),
                ("price_dollars", models.FloatField()),
                ("price_rubles", models.FloatField()),
                ("delivery_time", models.DateField()),
            ],
        ),
    ]
