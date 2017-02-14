from django.http import HttpResponse
from .models import Album

def index(request):
    allAlbums= Album.objects.all()
    html =''
    for album in allAlbums:
        url = '/music/' + str(album.id) + '/'
        html+='<a href="'+ url + '">' + album.albumTitle +'</a><br>'
    return HttpResponse(html)

def detail(request,albumId):
    return HttpResponse("<h2>Details for Album id: "+ str(albumId)+"</h2>")