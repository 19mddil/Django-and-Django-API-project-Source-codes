from django.urls import path
from users.views import PaitentRegistrationView, DoctorRegistrationView
app_name = 'users'
urlpatterns = [	
	path('registration/paitent/', PaitentRegistrationView.as_view(), name='register-paitent'),
	path('registration/doctor/', DoctorRegistrationView.as_view(), name='register-doctor'),
]