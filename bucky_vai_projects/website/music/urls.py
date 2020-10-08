from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
	# /music/
	path('', views.IndexView.as_view(), name='index'),

	# /music/71/
	path('<slug:pk>/',views.DetailView.as_view(),name='detail'),

	path('album/add/',views.AlbumCreate.as_view(),name='album-add'),


]