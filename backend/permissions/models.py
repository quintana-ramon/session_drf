from django.db import models

from departments.models import Department

# Create your models here.


class Permission(models.Model):
    departmentid = models.ForeignKey(Department, on_delete=models.CASCADE)
    save = models.BooleanField("Save", default=False)
    read = models.BooleanField("Read", default=False)
    update = models.BooleanField("Update", default=False)
    delete = models.BooleanField("Delete", default=False)
