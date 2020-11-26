from rest_framework import generics,permissions

from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly
from django.urls import reverse,reverse_lazy
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin


class PostList(generics.ListCreateAPIView):
	#permission_classes = (permissions.IsAuthenticated,)
	#How can only authinticated user able to create!!!
	#My Answer : https://stackoverflow.com/questions/49661615/django-rest-framework-listcreateapiview-not-checking-has-object-permissions
	#permission_classes = (IsAuthorOrReadOnly,)
	#queryset = Post.objects.all()
	serializer_class = PostSerializer
	permission_classes = (IsAuthorOrReadOnly,)
	def get_queryset(self):
	        """
	        This view should return a list of all the purchases
	        for the currently authenticated user.
	        """
	        user = self.request.user
	        if user.is_authenticated :
	        	return Post.objects.filter(author=user) 
	        else:
	        	return Post.objects.all()

	def perform_create(self, serializer):
		user = self.request.user
		if user.is_authenticated:
			serializer.save(author=user)
		else:
			serializer.save(author=None)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
	#permission_classes = (permissions.IsAuthenticated,)
	permission_classes = (IsAuthorOrReadOnly,)
	queryset = Post.objects.all()
	serializer_class = PostSerializer