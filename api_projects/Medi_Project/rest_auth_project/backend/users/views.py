from django.shortcuts import render
from rest_auth.registration.views import RegisterView
from rest_framework.permissions import IsAuthenticated
from users.serializers import (
	PaitentCustomRegistrationSerializer, 
	DoctorCustomRegistrationSerializer,
)

class PaitentRegistrationView(RegisterView):
	serializer_class = PaitentCustomRegistrationSerializer

class DoctorRegistrationView(RegisterView):
	serializer_class = DoctorCustomRegistrationSerializer

#Admin can list all the users
