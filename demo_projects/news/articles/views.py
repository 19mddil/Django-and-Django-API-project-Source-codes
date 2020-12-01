from django.views.generic import ListView,DetailView
from django.views.generic.edit import UpdateView,DeleteView,CreateView #new
from .models import Article
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (
	LoginRequiredMixin,
	UserPassesTestMixin # new
)
from pages.mixing import CustomLoginRequiredMixin
from django.contrib import messages

# Create your views here.

class ArticleListView(CustomLoginRequiredMixin,ListView):
	model = Article
	template_name = 'articles/article_list.html'
	login_url = 'login'
	permission_denied_message = 'You have to be logged in to access that article list page.'

class ArticleDetailView(CustomLoginRequiredMixin,DetailView):
	model = Article
	template_name = 'articles/article_detail.html'
	login_url = 'login'
	permission_denied_message = 'You have to be logged in for article detail page.'
	#success_url = reverse_lazy('article:article_detail') #if in model get_absolute_url not defined

class ArticleUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model = Article
	fields = ('title','body')
	template_name = 'articles/article_edit.html'
	login_url = 'login'
	permission_denied_message = 'You have to be logged in to edit article page.'

	def dispatch(self, request, *args, **kwargs):
	    if not request.user.is_authenticated:
	        messages.add_message(request, messages.WARNING,
	                             self.permission_denied_message)
	        return self.handle_no_permission()
	    return super(LoginRequiredMixin, self).dispatch(
	        request, *args, **kwargs
	    )
	def test_func(self): # new
		obj = self.get_object()
		return obj.author == self.request.user

class ArticleDeleteView(CustomLoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model = Article
	template_name = 'articles/article_delete.html'
	success_url = reverse_lazy('article_list')
	login_url = 'login'
	permission_denied_message = 'You have to be logged in for deleting an article'
	
	def test_func(self): # new
		obj = self.get_object()
		return obj.author == self.request.user


class ArticleCreateView(CustomLoginRequiredMixin,CreateView):
	model = Article
	template_name = 'articles/articles_new.html'
	fields = ('title','body')
	login_url = 'login'
	permission_denied_message = 'You have to be logged in for creating an article'

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)

