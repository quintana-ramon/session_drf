# Generated by Django 4.1.1 on 2022-09-26 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("permissions", "0002_permission_delete_adminuser_delete_financeuser_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="permission",
            name="delete",
            field=models.BooleanField(verbose_name="Delete"),
        ),
        migrations.AlterField(
            model_name="permission",
            name="read",
            field=models.BooleanField(verbose_name="Read"),
        ),
        migrations.AlterField(
            model_name="permission",
            name="save",
            field=models.BooleanField(verbose_name="Save"),
        ),
        migrations.AlterField(
            model_name="permission",
            name="update",
            field=models.BooleanField(verbose_name="Update"),
        ),
    ]
