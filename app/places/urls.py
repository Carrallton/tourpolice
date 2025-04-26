from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CachedPlacesView

router = DefaultRouter()
router.register(r'places', CachedPlacesView)

urlpatterns = [
    path('', include(router.urls)),
]