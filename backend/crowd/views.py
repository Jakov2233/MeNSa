from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def kolicina_guzve(request):
    data = {
        'ljudi': 123,
        'nivo': 'srednji',
    }

    return Response(data)

