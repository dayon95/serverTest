from django.shortcuts import render
from django.http import HttpResponse
from .models import PosterData
# Create your views here.

def post_list(request):

    posts = PosterData.objects.all()
    return render(request, 'data01/post_list.html', {'posts': posts})

#def detail(request, pk):

#    photo=PosterData.objects.get(pk=pk)
#    msg = (
#        '<p>{pk} poster</p>'.format(pk=photo.pk),
#        '<p>url}></p>'.format(url=photo.image.url),
#        '<p><img src="{url}" \></p>'.format(url=photo.image.url)
#        )
#    return HttpResponse('\n'.join(msg))
