from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny, SAFE_METHODS
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from applications.users.models.user import User
from applications.users.serializers import RegisterUserSerializer, UserListSerializer
from applications.users.utils import set_jwt_cookies


class RegisterUserAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return UserListSerializer
        return RegisterUserSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        response = Response(
            data=serializer.data,
            status=status.HTTP_201_CREATED
        )
        set_jwt_cookies(response, user)
        return response

class LogInAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request: Request) -> Response:
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(
            request=request,
            username=username,
            password=password
        )

        if user:
            response = Response(
                status=status.HTTP_200_OK
            )

            set_jwt_cookies(response=response, user=user)

            return response

        else:
            return Response(
                data={"message": "Invalid username or password."},
                status=status.HTTP_401_UNAUTHORIZED
            )


class LogOutAPIView(APIView):
    def post(self, request):
        response = Response(status=status.HTTP_200_OK)

        response.delete_cookie('access_token')
        response.delete_cookie('refresh_token')

        return response

# class RegisterUserAPIView(APIView):
#     permission_classes = [AllowAny]
#
#     def get (self, request) -> Response:
#         serializer = UserListSerializer(data=request.data)
#         if serializer.is_valid():
#             response = Response(
#                 data=serializer.data,
#                 status=status.HTTP_200_OK
#             )
#
#         return response
#
#     def post(self, request: Request) -> Response:
#         serializer = RegisterUserSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         response = Response(
#             data=serializer.data,
#             status=status.HTTP_201_CREATED
#         )
#
#         return response
