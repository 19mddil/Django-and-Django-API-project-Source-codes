from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
	# /music/
	path('', views.index, name='index'),

	# /music/71/
	path('<int:album_id>/',views.detail,name='detail'),
]