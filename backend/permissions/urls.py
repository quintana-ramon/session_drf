from django.urls import path, include

from . import views

# 127.0.0.1:8000/api/v1/user
urlpatterns = [
    path("", views.admin_user_create_view),
]
