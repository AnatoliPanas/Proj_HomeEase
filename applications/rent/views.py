from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import SAFE_METHODS

from applications.rent.models import Rent
from applications.rent.serializers import RentListSerializer, RentCreateSerializer


class RentListCreateGenericAPIView(ListCreateAPIView):
    queryset = Rent.objects.all()

    def get_serializer_class(self):
        if self.request.method == SAFE_METHODS:
            return RentListSerializer
        return RentCreateSerializer
