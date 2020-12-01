from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView #new
from .models import Post
from django.urls import reverse_lazy
# Create your views here.

class BlogListView(ListView): #read

	model = Post
	template_name = 'blog/home.html'

class BlogDetailView(DetailView): #read

	model = Post
	template_name = 'blog/post_detail.html'

class BlogCreateView(CreateView): #create

	model = Post
	template_name = 'blog/post_new.html'
	fields = ['title','author','body']

class BlogUpdateView(UpdateView): #update

	model = Post
	template_name = 'blog/post_edit.html'
	fields = ['title','body']

class BlogDeleteView(DeleteView): #delete

	model = Post
	template_name = 'blog/post_delete.html'
	success_url = reverse_lazy('home')

