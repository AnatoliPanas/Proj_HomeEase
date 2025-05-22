from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import status, filters
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView,
                                     get_object_or_404,
                                     RetrieveAPIView,
                                     ListAPIView)
from rest_framework.permissions import SAFE_METHODS
from rest_framework.response import Response
from rest_framework.views import APIView

from applications.rent.models.locations import Address
from applications.rent.models.rent import Rent
from applications.rent.serializers import (RentListSerializer,
                                           RentCreateSerializer,
                                           RentSwitchActiveSerializer,
                                           RentDetailSerializer,

                                           AddressListSerializer,
                                           AddressCreateSerializer)


class AddressListCreateGenericAPIView(ListCreateAPIView):
    queryset = Address.objects.all()

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return AddressListSerializer
        return AddressCreateSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]

    filterset_fields = ['postal_code', 'country', 'city', 'street']
    search_fields = ['country', 'city', 'street']
    ordering_fields = ['created_at']


class RentListCreateGenericAPIView(ListCreateAPIView):
    queryset = Rent.objects.all()

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return RentListSerializer
        return RentCreateSerializer


class TestRentDetailUpdateDeleteGenericAPIView(RetrieveAPIView):
    queryset = Rent.objects.all()
    lookup_url_kwarg = 'rent_id'
    serializer_class = RentDetailSerializer


class RentDetailUpdateDeleteGenericAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Rent.objects.all()
    lookup_url_kwarg = 'rent_id'

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            print("RentDetailSerializer", "=" * 30)
            return RentDetailSerializer
        else:
            print("RentCreateSerializer", "=" * 30)
        return RentCreateSerializer

    def partial_update(self, request, *args, **kwargs):
        data = request.data
        instance = self.get_object()
        # serializer = RentCreateSerializer(instance=instance, data=data, partial=True)
        serializer = self.get_serializer(instance=instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class RentSwitchActiveAPIView(APIView):
    def patch(self, request, rent_id):
        rent = get_object_or_404(Rent, id=rent_id, is_deleted=False)
        rent.is_active = not rent.is_active
        rent.save()
        serializer = RentSwitchActiveSerializer(rent)
        return Response(serializer.data, status=status.HTTP_200_OK)
