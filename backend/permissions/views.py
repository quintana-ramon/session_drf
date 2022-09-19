from rest_framework import generics

from .models import AdminUser, FinanceUser, PurchasingUser, SalesUser
from .serializers import AdminUserSerializer

# Create your views here.


class CreateUser(generics.CreateAPIView):
    queryset = AdminUser.objects.all()
    serializer_class = AdminUserSerializer


admin_user_create_view = CreateUser.as_view()
