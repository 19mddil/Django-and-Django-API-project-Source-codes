from django.views.generic import ListView,DetailView
from django.views.generic.edit import UpdateView,DeleteView,CreateView #new
from .models import Article
from django.urls import reverse_lazy
# Create your views here.

class ArticleListView(ListView):
	model = Article
	template_name = 'articles/article_list.html'

class ArticleDetailView(DetailView):
	model = Article
	template_name = 'articles/article_detail.html'

class ArticleUpdateView(UpdateView):
	model = Article
	fields = ('title','body')
	template_name = 'articles/article_edit.html'

class ArticleDeleteView(DeleteView):
	model = Article
	template_name = 'articles/article_delete.html'
	success_url = reverse_lazy('article_list')

class ArticleCreateView(CreateView):
	model = Article
	template_name = 'articles/articles_new.html'
	fields = ('title','body')

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)
