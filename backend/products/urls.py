from django.urls import path

from . import views

# 127.0.0.1:8000/api/v1/products/
urlpatterns = [
    path("", views.product_view),
]
