from django.db import models

# Create your models here.

class Song(models.Model):
    song_title = models.CharField(max_length= 50)
    song_album = models.CharField(max_length= 50)
    song_review = models.TextField()
    song_link = models.CharField(max_length= 200)

    def __str__(self):
        return self.song_title
