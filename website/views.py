from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.core.mail import send_mail
from . import models

# Create your views here.
def home(request):
    return render(request, 'website/home.html', context=locals())

class Music(ListView):
    model = models.Album
    context_object_name = 'music'
    template_name= 'website/music.html'

class Album(DetailView):
    model = models.Album
    context_object_name = 'album'
    template_name = 'website/album.html'

def contact(request):
    return render(request,'website/contact.html', context=locals())

def submit(request):
    if request.method == "POST":
        email = request.POST['email']
        message = request.POST['message']
        reason = request.POST['reason']
        send_mail(
            'Contact from email',
            reason + "\n" + message,
            'web@hyerion.com',
            ['quin@ikhodi.tech',],
            fail_silently=False
        )

        return render(request, 'website/contact.html', { 'success' : "Awesome, we'll contact you" })
    else:
        return render(request, 'website/contact.html', context=locals())
