from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView #new
from .models import Post
# Create your views here.

class BlogListView(ListView):
	model = Post
	template_name = 'blog/home.html'

class BlogDetailView(DetailView):
	model = Post
	template_name = 'blog/post_detail.html'

class BlogCreateView(CreateView):
	model = Post
	template_name = 'blog/post_new.html'
	fields = ['title','author','body']