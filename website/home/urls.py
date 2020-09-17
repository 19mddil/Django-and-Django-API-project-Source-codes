from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
	# /home/
	path('home/', views.index, name='index'),


]