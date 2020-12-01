from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth import views as auth_views
from pages.mixing import CustomLoginRequiredMixin

class SignUpView(CreateView):
	form_class = CustomUserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'users/signup.html'


class PasswordChangeView(CustomLoginRequiredMixin,auth_views.PasswordChangeView):
    template_name = 'users/registration/password_change_form.html'
    permission_denied_message = 'you have to be first logged in'
    login_url = 'login'

class LoginView(auth_views.LoginView):
	template_name = 'users/registration/login.html'

class PasswordChangeDoneView(auth_views.PasswordChangeDoneView):
	template_name = 'users/registration/password_change_done.html'

class PasswordResetView(auth_views.PasswordResetView):
	template_name = 'users/registration/password_reset_form.html'
	email_template_name = 'users/registration/password_reset_email.html'

class PasswordResetDoneView(auth_views.PasswordResetDoneView):
	template_name = 'users/registration/password_reset_done.html'

class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
	template_name = 'users/registration/password_reset_complete.html'

class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
	template_name = 'users/registration/password_reset_confirm.html'