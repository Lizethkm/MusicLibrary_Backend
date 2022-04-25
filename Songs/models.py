
from django.db import models

# Create your models here.


class Songs(models.Model):
    title = models.CharField(max_length=250)
    artist = models.CharField(max_length=250)
    album = models.CharField(max_length=250)
    release_date = models.DateField(max_length=250)
    genre = models.CharField(max_length=250)