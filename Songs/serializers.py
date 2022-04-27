from rest_framework import serializers
from .models import Song, Songs



class SongSerializer(serializers.ModelsSerializer()):
    class Meta:
        model = Song
        fields =['title', 'artist', 'album', 'release_date', 'genre']