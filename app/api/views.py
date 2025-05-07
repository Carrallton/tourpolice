from rest_framework import viewsets, generics, permissions
from .models import News, EmergencyRequest
from .serializers import NewsSerializer, EmergencyRequestSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAuthenticated]

class EmergencyCreate(generics.CreateAPIView):
    queryset = EmergencyRequest.objects.all()
    serializer_class = EmergencyRequestSerializer
    permission_classes = [permissions.IsAuthenticated]