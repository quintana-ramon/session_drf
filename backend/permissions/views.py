from sys import maxsize
from rest_framework import generics
from rest_framework import mixins

from .models import Permission
from .serializers import PermissionSerializer

# Create your views here.


class PermissionAPIView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    lookup_field = "pk"

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


permission_view = PermissionAPIView.as_view()
