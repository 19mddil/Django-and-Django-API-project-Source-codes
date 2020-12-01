from django.urls import path
from .views import UserList,UserDetail,PostList,PostDetail
from django.contrib.auth import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
	path('<int:pk>/',PostDetail.as_view()),
	path('',PostList.as_view()),
	path('users/',UserList.as_view()),
	path('users/<int:pk>/',UserDetail.as_view()),
]
