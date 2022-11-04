from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from drinkapp.models import Drink
from DrinkApi.serializers import DrinkSerializer
from django.http import JsonResponse

# Create your views here.
# @api_view(['GET'])
def drinkList(request):

    # Get all the drinks
    # Serialize them
    # Return json
    drinks = Drink.objects.all()
    serializer = DrinkSerializer(drinks, many=True)
    return Response(serializer.data)
