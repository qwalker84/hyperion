from django.db import models

# Create your models here.
class Album(models.Model):
    name = models.CharField('Name', max_length=140)
    cover_art = models.ImageField(upload_to="album_art")
    release_date = models.DateField()

    def __str__(self):
        return self.name

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete='CASCADE')
    name = models.CharField(max_length=100)
    number = models.PositiveIntegerField()

    def __str__(self):
        return self.name