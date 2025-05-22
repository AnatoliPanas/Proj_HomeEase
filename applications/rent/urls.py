from django.urls import path

from applications.rent.views import (RentListCreateGenericAPIView,
                                     RentDetailUpdateDeleteGenericAPIView,
                                     RentSwitchActiveAPIView,
                                     TestRentDetailUpdateDeleteGenericAPIView,
                                     AddressListCreateGenericAPIView
                                     )

urlpatterns = [
    path('rent/', RentListCreateGenericAPIView.as_view()),
    path('rent/<int:rent_id>', RentDetailUpdateDeleteGenericAPIView.as_view()),
    path('rent/<int:rent_id>/switch-active/', RentSwitchActiveAPIView.as_view()),
    path('renttest/<int:rent_id>', TestRentDetailUpdateDeleteGenericAPIView.as_view()),

    path('address/', AddressListCreateGenericAPIView.as_view()),

]
