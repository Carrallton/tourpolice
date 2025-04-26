import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from chatbot.routing import websocket_urlpatterns
from chatbot.middleware import JWTAuthMiddleware
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

application = ProtocolTypeRouter({
    "websocket": JWTAuthMiddleware(
        URLRouter(websocket_urlpatterns)
    ),
})
