from tabnanny import verbose
from django.db import models

# Create your models here.


class Department(models.Model):
    name = models.CharField("Department Name", max_length=25, blank=False, null=False)

    class Meta:
        verbose_name_plural = "Departments"
        abstract = False
