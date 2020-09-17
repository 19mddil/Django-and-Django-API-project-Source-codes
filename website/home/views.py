from django.http import HttpResponse
from django.template import loader
from django.urls import reverse,reverse_lazy

def index(request):
	template = loader.get_template('home/index.html')
	url_to_music_home = reverse_lazy('music:index')
	#If we had to pass in a param we would use reverse here.
	context ={'home':url_to_music_home}
	return HttpResponse(template.render(context,request))