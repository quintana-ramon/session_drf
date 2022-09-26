from django.db import models

from permissions.models import Permission

# Create your models here.


class Product(models.Model):
    name = models.CharField("Name", max_length=25, blank=False, null=False)
    amount = models.BigIntegerField("Amount", blank=False, null=False)
    description = models.CharField(
        "Description", max_length=50, blank=False, null=False
    )
    permissions = models.ForeignKey(Permission, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Products"
        abstract = False
