# Generated by Django 5.1 on 2024-09-05 16:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Organizador",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=150)),
                ("apellido", models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name="Eventos",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=150)),
                ("hora", models.TimeField()),
                ("fecha", models.DateField()),
                ("lugar", models.CharField(max_length=100)),
                ("descripcion", models.TextField()),
                (
                    "organizador",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="eventos.organizador",
                    ),
                ),
            ],
        ),
    ]
