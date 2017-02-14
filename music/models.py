from django.db import models

# Red primary Key 1
class Album(models.Model):
    artist = models.CharField(max_length=250)
    albumTitle = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    albumLogo = models.CharField(max_length=1000)

    def __str__(self):
        return(self.albumTitle+ ' - '+self.artist)

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE) #delete all the songs if an album is delete
    fileType = models.CharField(max_length=10)
    songTitle = models.CharField(max_length=250)

    def __str__(self):
        return(self.album +' - '+self.songTitle)
