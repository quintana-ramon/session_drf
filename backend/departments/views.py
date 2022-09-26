import re
from sys import maxsize
from rest_framework import generics
from rest_framework import mixins

from .models import Department
from .serializers import DepartmentSerializer

# Create your views here.


class PermissionAPIView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("id")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):

        return self.create(request, *args, **kwargs)


department_view = PermissionAPIView.as_view()
