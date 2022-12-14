# Generated by Django 4.1.1 on 2022-09-26 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("permissions", "0002_permission_delete_adminuser_delete_financeuser_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=25, verbose_name="Name")),
                ("amount", models.BigIntegerField(verbose_name="Amount")),
                (
                    "description",
                    models.CharField(max_length=50, verbose_name="Description"),
                ),
                (
                    "permissions",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="permissions.permission",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Products",
                "abstract": False,
            },
        ),
    ]
