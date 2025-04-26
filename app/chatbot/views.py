from rest_framework import viewsets
from .models import ChatMessage
from .serializers import ChatMessageSerializer

class ChatMessageViewSet(viewsets.ModelViewSet):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer