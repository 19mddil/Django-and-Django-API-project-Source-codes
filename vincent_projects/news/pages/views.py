from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

class HomePageView(LoginRequiredMixin,TemplateView):
	template_name = 'users/home.html'
	login_url = 'login' #new
	permission_denied_message = 'You have to be logged in to access the home page and view articles.'

	def dispatch(self, request):
	    if not request.user.is_authenticated:
	        messages.add_message(request, messages.WARNING,
	                             self.permission_denied_message)
	        return self.handle_no_permission()
	    return super(LoginRequiredMixin,self).dispatch(request)