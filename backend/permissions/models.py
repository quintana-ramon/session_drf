from django.db import models

from departments.models import Department
from products.models import Product

# Create your models here.


class Permission(models.Model):
    PERMISSIONS_CHOISES = (
        ("s", "Save"),
        ("r", "Read"),
        ("u", "Update"),
        ("d", "Delete"),
    )
    productid = models.ForeignKey(Product, on_delete=models.CASCADE)
    departmentid = models.ForeignKey(Department, on_delete=models.CASCADE)
    permissions = models.CharField(
        "Permissions", max_length=1, choices=PERMISSIONS_CHOISES
    )
