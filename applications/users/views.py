from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from applications.users.models.user import User
from applications.users.serializers import RegisterUserSerializer, UserListSerializer

class RegisterUserAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserListSerializer
        return RegisterUserSerializer

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
