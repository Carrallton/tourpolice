from rest_framework import viewsets, generics, permissions
from .models import News, EmergencyRequest
from .serializers import NewsSerializer, EmergencyRequestSerializer
from rest_framework.permissions import IsAuthenticated

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class EmergencyViewSet(viewsets.ModelViewSet):
    queryset = EmergencyRequest.objects.all()
    serializer_class = EmergencyRequestSerializer
    permission_classes = [permissions.IsAuthenticated]