from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth import views as auth_views

class SignUpView(CreateView):
	form_class = CustomUserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'users/signup.html'


class PasswordChangeView(auth_views.PasswordChangeView):
    template_name = 'users/registration/password_change_form.html'

class LoginView(auth_views.LoginView):
	template_name = 'users/registration/login.html'

class PasswordChangeDoneView(auth_views.PasswordChangeDoneView):
	template_name = 'users/registration/password_change_done.html'