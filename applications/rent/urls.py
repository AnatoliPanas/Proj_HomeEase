from django.urls import path

from applications.rent.views import RentListCreateGenericAPIView

urlpatterns = [
    path('rent/', RentListCreateGenericAPIView.as_view()),
]