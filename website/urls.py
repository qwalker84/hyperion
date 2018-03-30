from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import ListView, DetailView
from . import views

app_name = 'website'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^music/$', views.Music.as_view(), name="music"),
    url(r'^music/album/(?P<pk>[\w-]+)/$', views.Album.as_view(), name="album"),
    url(r'^contact/$', views.contact, name="contact"),
    url(r'^contact/submit/$',views.submit, name="submit")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
