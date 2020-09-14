from django.http import Http404
#from django.http import HttpResponse
#from django.template import loader
from django.shortcuts import render
from .models import Album

def index(request):
	all_albums = Album.objects.all()
	#template = loader.get_template('music/index.html')
	#context = {'all_albums':all_albums,}
	#html = ''
	#for album in all_albums:
	#	url = '/music/'+str(album.id)+'/'
	#	html += '<a href="'+url+'">'+album.album_title+'</a><br>'
	#return HttpResponse(html)
	#return HttpResponse(template.render(context,request))
	return render(request,'music/index.html',{'all_albums':all_albums}) #Behind the scene it return an http response.


def detail(request,album_id):
	#return HttpResponse("<h2>Details for Album id : "+ str(album_id)+ "</h2>")
	try:
		album = Album.objects.get(pk=album_id)
	except Album.DoesNotExist:
		raise Http404("Album does not exist")
	return render(request,'music/details.html',{'album':album})
