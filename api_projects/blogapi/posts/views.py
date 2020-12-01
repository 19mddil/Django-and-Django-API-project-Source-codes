from rest_framework import generics,permissions
from django.contrib.auth import get_user_model

from .models import Post
from .serializers import PostSerializer,UserSerializer
from .permissions import IsAuthorOrReadOnly,IsUserOrReadOnly
#from rest_framework.response import Response
#from rest_framework import status,viewsets
from django.core.exceptions import PermissionDenied

class PostList(generics.ListCreateAPIView):
	#permission_classes = (permissions.IsAuthenticated,)
	#How can only authinticated user able to create!!!
	#My Answer : https://stackoverflow.com/questions/49661615/django-rest-framework-listcreateapiview-not-checking-has-object-permissions
	#permission_classes = (IsAuthorOrReadOnly,)
	#queryset = Post.objects.all()
	serializer_class = PostSerializer
	permission_classes = (IsAuthorOrReadOnly,)
	# I will let only authenticated users to see only their posts not others!
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
		# I will let only authenticated user to create posts
		if user.is_authenticated:
			serializer.save(author=user)
		else:
			#serializer.save(author=None)
			#content = {'error': 'IntegrityError'}
			#return Response(content, status=status.HTTP_400_BAD_REQUEST)
			raise PermissionDenied("You do not have permission to Create posts :(")

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
	#permission_classes = (permissions.IsAuthenticated,)
	#I won't let others to alter others content
	permission_classes = (IsAuthorOrReadOnly,)
	queryset = Post.objects.all()
	serializer_class = PostSerializer


class UserList(generics.ListCreateAPIView):
	queryset = get_user_model().objects.all()
	serializer_class = UserSerializer

	def perform_create(self, serializer):
		user = self.request.user
		#I will let only admin to create new user!
		if user.is_staff:
			serializer.save()
		else:
			raise PermissionDenied("You do not have permission to Create user :(")

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = get_user_model().objects.all()
	serializer_class = UserSerializer
	#I won't let others to alter others except admin
	permission_classes = (IsUserOrReadOnly,)
	#def destroy(self, request, *args, **kwargs):
		#try:
			#if self.request.user.id == self.get_object().id :
				#instance = self.get_object()
				#self.perform_destroy(instance)
		#except Http404:
		    #pass
		#return Response(status=status.HTTP_204_NO_CONTENT)
	#def perform_destroy(self, serializer):
		#username = self.request.username
		#if user.is_authenticated:
			#serializer.save(author=user)
		#else:
			#serializer.save(author=None)
			#content = {'error': 'IntegrityError'}
			#return Response(content, status=status.HTTP_400_BAD_REQUEST)
			#raise PermissionDenied("You do not have permission to Enter Clients in Other Company, Be Careful")