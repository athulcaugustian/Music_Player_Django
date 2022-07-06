from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Song(models.Model):

    Language_Choice = (
              ('Hindi', 'Hindi'),
              ('English', 'English'),
              ('Malayalam','Malayalam')
          )

    

    name = models.CharField(max_length=20)
    album = models.CharField(max_length=20)
    language = models.CharField(max_length=20,choices=Language_Choice)
    song_img = models.FileField()
    year = models.IntegerField()
    lyrics=models.TextField()
    singer = models.CharField(max_length=200)
    song_file = models.FileField()

    def __str__(self):
        return self.name


class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    playlist_name = models.CharField(max_length=200)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)


class Favourite(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    is_fav = models.BooleanField(default=False)


class Recent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

# class comments(models.Model):
#     song = models.ForeignKey(Song, on_delete=models.CASCADE, default=1)
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     review=models.CharField(max_length=200)