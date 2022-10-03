from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status, generics, mixins, authentication, permissions

from .models import User
from .serializers import UserSerializer

# Create your views here.


class CreateUser(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        user = self.create(request, *args, **kwargs)
        token, created = Token.objects.get_or_create(user=user)

        return Response(
            {"token": token.key, "user_id": user["id"], "email": user["email"]},
            status=status.HTTP_201_CREATED,
        )

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.validated_data

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


user_view = CreateUser.as_view()
