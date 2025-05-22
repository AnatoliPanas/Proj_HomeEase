from django.urls import path

from applications.users.views import RegisterUserAPIView

urlpatterns = [
    path('auth-register/', RegisterUserAPIView.as_view()),
]