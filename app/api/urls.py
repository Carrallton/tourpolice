from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NewsViewSet, EmergencyCreate

router = DefaultRouter()
router.register(r'news', NewsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('emergency/', EmergencyCreate, name='emergency-create'),
]