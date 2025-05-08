from django.db import models
from accounts.models import CustomUser

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=50)
    region = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class EmergencyRequest(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    lat = models.FloatField()
    lon = models.FloatField()
    emergency_type = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)