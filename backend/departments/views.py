from rest_framework import generics, mixins, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication

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
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("id")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):

        return self.create(request, *args, **kwargs)


department_view = PermissionAPIView.as_view()
