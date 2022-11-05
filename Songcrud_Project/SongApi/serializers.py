from rest_framework import serializers
from Music_app.models import Artiste, Song, Lyric

class ArtisteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artiste
        fields = '__all__'

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'

# class UpdateSongSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Song
#         fields = '__all__'