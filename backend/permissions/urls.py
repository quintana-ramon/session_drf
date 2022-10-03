from django.urls import path

from . import views

# 127.0.0.1:8000/api/v1/permissions/
urlpatterns = [
    path("", views.permission_view),
    path("<int:pk>/", views.permission_view),
]
