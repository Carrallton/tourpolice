from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NewsViewSet, EmergencyViewSet
from places.views import CachedPlacesView
from chatbot.views import ChatMessageViewSet

router = DefaultRouter()
router.register(r'news', NewsViewSet)
router.register(r'emergency', EmergencyViewSet)
router.register(r'places', CachedPlacesView)
router.register(r'chat', ChatMessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]