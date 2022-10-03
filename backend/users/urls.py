from django.urls import path
from rest_framework_simplejwt.views import (
    token_obtain_pair,
    TokenRefreshView,
    TokenVerifyView,
)
from . import views

# 127.0.0.1:8000/api/v1/users/
urlpatterns = [
    path("", views.user_view),
    path("<int:pk>/", views.user_view),
    path("token/", token_obtain_pair, name="token_obtain_pair"),
]
