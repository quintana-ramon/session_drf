from django.db import models

from departments.models import Department

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField("Email", max_length=20, unique=True)
    password = models.CharField("Password", max_length=50)
    name = models.CharField("Name", max_length=40, blank=False, null=False)
    last_name = models.CharField("Last Name", max_length=40, blank=False, null=False)
    departmentid = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Users"
        abstract = False
