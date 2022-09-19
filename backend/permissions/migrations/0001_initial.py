# Generated by Django 4.1.1 on 2022-09-19 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AdminUser",
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
                ("username", models.CharField(max_length=20, unique=True)),
                (
                    "email",
                    models.EmailField(max_length=20, unique=True, verbose_name="Email"),
                ),
                ("password", models.CharField(max_length=50, verbose_name="Password")),
                ("name", models.CharField(max_length=40, verbose_name="Name")),
                (
                    "last_name",
                    models.CharField(max_length=40, verbose_name="Last Name"),
                ),
            ],
            options={
                "verbose_name_plural": "Administrador",
            },
        ),
        migrations.CreateModel(
            name="FinanceUser",
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
                ("username", models.CharField(max_length=20, unique=True)),
                (
                    "email",
                    models.EmailField(max_length=20, unique=True, verbose_name="Email"),
                ),
                ("password", models.CharField(max_length=50, verbose_name="Password")),
                ("name", models.CharField(max_length=40, verbose_name="Name")),
                (
                    "last_name",
                    models.CharField(max_length=40, verbose_name="Last Name"),
                ),
            ],
            options={
                "verbose_name_plural": "Finanzas",
            },
        ),
        migrations.CreateModel(
            name="PurchasingUser",
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
                ("username", models.CharField(max_length=20, unique=True)),
                (
                    "email",
                    models.EmailField(max_length=20, unique=True, verbose_name="Email"),
                ),
                ("password", models.CharField(max_length=50, verbose_name="Password")),
                ("name", models.CharField(max_length=40, verbose_name="Name")),
                (
                    "last_name",
                    models.CharField(max_length=40, verbose_name="Last Name"),
                ),
            ],
            options={
                "verbose_name_plural": "Compras",
            },
        ),
        migrations.CreateModel(
            name="SalesUser",
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
                ("username", models.CharField(max_length=20, unique=True)),
                (
                    "email",
                    models.EmailField(max_length=20, unique=True, verbose_name="Email"),
                ),
                ("password", models.CharField(max_length=50, verbose_name="Password")),
                ("name", models.CharField(max_length=40, verbose_name="Name")),
                (
                    "last_name",
                    models.CharField(max_length=40, verbose_name="Last Name"),
                ),
            ],
            options={
                "verbose_name_plural": "Ventas",
            },
        ),
    ]