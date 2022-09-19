from django.db import models

# Create your models here.


class UserInterface(models.Model):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField("Email", max_length=20, unique=True)
    password = models.CharField("Password", max_length=50)
    name = models.CharField("Name", max_length=40, blank=False, null=False)
    last_name = models.CharField("Last Name", max_length=40, blank=False, null=False)

    class Meta:
        abstract = True


class AdminUser(UserInterface):
    class Meta:
        verbose_name_plural = "Administrador"


class SalesUser(UserInterface):
    class Meta:
        verbose_name_plural = "Ventas"


class PurchasingUser(UserInterface):
    class Meta:
        verbose_name_plural = "Compras"


class FinanceUser(UserInterface):
    class Meta:
        verbose_name_plural = "Finanzas"
