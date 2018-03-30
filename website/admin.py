from django.contrib import admin
from . import models


# Register your models here.
class SongInline(admin.StackedInline):
    model = models.Song

class AlbumAdmin(admin.ModelAdmin):
    model = models.Album
    inlines = (SongInline,)

admin.site.register(models.Album, AlbumAdmin)