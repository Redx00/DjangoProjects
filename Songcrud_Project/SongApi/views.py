from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from Music_app.models import Song, Artiste, Lyric
from .serializers import ArtisteSerializer, SongSerializer
from rest_framework import status
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser


# Create your views here.
@api_view(['GET'])
def getArtisteData(request):
    artiste = Artiste.objects.all()
    serializer = ArtisteSerializer(artiste, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getSongData(request):
    song = Song.objects.all()
    serializer = SongSerializer(song, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def Song_detail(request, id):
    if request.method == 'GET': 
        serializer = SongSerializer(Song) 
        return JsonResponse(serializer.data) 
 
    elif request.method == 'PUT': 
        song_data = JSONParser().parse(request) 
        serializer = SongSerializer(Song, data=song_data) 
        if serializer.is_valid(): 
            serializer.save() 
            return JsonResponse(serializer.data) 
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        Song.delete() 
        return JsonResponse({'message': 'Song was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

# @api_view(['POST'])
# def UpdateSongData(request, id):
# 	Updatesong = Song.objects.get(id=id)
# 	serializer = UpdateSongSerializer(instance=Updatesong, data=request.data)
#     return Response (serializer.data)

# @api_view(['PATCH'])
# def UpdateSongData(request, id):
#     Updatesong = Song.objects.get(id=id)
#     serializer = UpdateSongSerializer(Updatesong, many=True)
#     return Response(serializer.data)
    # if serializer.is_valid():
    #     serializer.save()
    #     return Response(serializer.data)
	# else:
    #     return Response(status=status.HTTP_404_NOT_FOUND)