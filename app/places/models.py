from django.db import models

class Place(models.Model):
    CATEGORY_CHOICES = [
        ('historical', 'Историческое место'),
        ('entertainment', 'Развлечения'),
        ('food', 'Еда'),
        ('education', 'Образование'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    latitude = models.FloatField()  # Широта
    longitude = models.FloatField()  # Долгота
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name