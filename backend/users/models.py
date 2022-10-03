from django.db import models
from django.contrib.auth.models import User
from departments.models import Department

# Create your models here.


class MyUser(User):
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)
