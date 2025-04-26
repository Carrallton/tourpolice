from django.urls import path
from .consumers import ChatBotConsumer

websocket_urlpatterns = [
    path('ws/chat/', ChatBotConsumer.as_asgi()),
]