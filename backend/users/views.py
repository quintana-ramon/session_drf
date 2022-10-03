# from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status, generics, mixins, authentication, permissions
from rest_framework_simplejwt.tokens import Token

from .serializers import UserSerializer
from .models import MyUser

# Create your views here.


class CreateUser(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer
    # authentication_classes = [authentication.SessionAuthentication]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # token = Token.for_user(user)

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


user_view = CreateUser.as_view()


# class MyToken(Token):
#     def for_user(cls, user):
#         user_id = getattr(user, api_settings.USER_ID_FIELD)
#         if not isinstance(user_id, int):
#             user_id = str(user_id)

#         token = cls()
#         token[api_settings.USER_ID_CLAIM] = user_id

#         return token
