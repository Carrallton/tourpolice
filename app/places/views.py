from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Place
from rest_framework import viewsets
from .models import Place
from .serializers import PlaceSerializer

class CachedPlacesView(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
