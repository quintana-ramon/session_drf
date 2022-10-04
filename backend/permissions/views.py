from rest_framework import generics, mixins, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Permission
from .serializers import PermissionSerializer
from .customPermission import CustomPermission

# Create your views here.


class PermissionAPIView(
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    lookup_field = "pk"
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


permission_view = PermissionAPIView.as_view()
