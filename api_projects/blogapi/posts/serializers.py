from django.contrib.auth import get_user_model #new
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
	class Meta:
		fields = ('id','author','title','body','created_at',)
		read_only_fields = ('author',)
		model = Post

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = get_user_model()
		fields = ('id','username',)
		#read_only_fields = ('username',)