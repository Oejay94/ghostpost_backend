from django.db import models
from django.utils import timezone


class BoastRoast(models.Model):
    Boast = 'Boast'
    Roast = 'Roast'
    CHOICES = [
        (Boast, 'Boast'),
        (Roast, 'Roast')
    ]
    title = models.CharField(max_length=50)
    boast_or_roast = models.CharField(max_length=5, choices=CHOICES, default=Boast)
    body = models.TextField()
    total_count = models.IntegerField(default=0)
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
