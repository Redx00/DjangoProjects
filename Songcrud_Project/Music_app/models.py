from django.db import models
from datetime import datetime

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name

class Song(models.Model):
    # Choices
    LIKES = (
    (0, 'Low'),
    (1, 'Normal'),
    (2, 'High'),
    )
 
    artiste_id= models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    date_released = models.DateField(default = datetime.today)
    like = models.IntegerField(default=0, choices=LIKES)

    def __str__(self):
        return self.title

class Lyric(models.Model):
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)

    def __str__(self):
        return self.content