from django.urls import path
from .views import SignUpView,PasswordChangeView,LoginView,PasswordChangeDoneView,PasswordResetView,PasswordResetDoneView,PasswordResetCompleteView,PasswordResetConfirmView
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('signup/',SignUpView.as_view(),name='signup'),
	path('password_change/', PasswordChangeView.as_view() , name='password_change'),

	path('password_change/done/', PasswordChangeDoneView.as_view() , name='password_change_done'),
	path('password_reset/',PasswordResetView.as_view(),name='password_reset'),
	path('password_reset/done/',PasswordResetDoneView.as_view(),name='password_reset_done'),
	path('reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
	path('reset/done/',PasswordResetCompleteView.as_view(),name='password_reset_complete'),
	path('login/',LoginView.as_view(),name='login'),
]