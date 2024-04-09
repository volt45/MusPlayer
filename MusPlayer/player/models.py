from django.db import models


class Music(models.Model):
    Url = models.URLField()
    Name = models.CharField(max_length=250)
    Autor = models.CharField(max_length=250)
    Album = models.CharField(max_length=250)
    Duration = models.IntegerField()
    DateReleased = models.DateField()


class Album(models.Model):
    ImageAlbum = models.ImageField()
    DateReleased = models.DateField()
    MusicID = models.ForeignKey(Music, on_delete=models.CASCADE, default=None, blank=True, null=True)


class User(models.Model):
    FirstName = models.CharField(max_length=150)
    LastName = models.CharField(max_length=150)
    Login = models.CharField(max_length=250)
    Password = models.CharField(max_length=50)
    Phone = models.CharField(max_length=50)
    Email = models.EmailField()
    DateBirth = models.DateField()
