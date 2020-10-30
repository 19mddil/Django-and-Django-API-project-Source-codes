from django.urls import path
from .views import SignUpView,PasswordChangeView,LoginView,PasswordChangeDoneView
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('signup/',SignUpView.as_view(),name='signup'),
	path('password_change/', PasswordChangeView.as_view() , name='password_change'),

	path('password_change/done/', PasswordChangeDoneView.as_view() , name='password_change_done'),
	path('login/',LoginView.as_view(),name='login'),
]