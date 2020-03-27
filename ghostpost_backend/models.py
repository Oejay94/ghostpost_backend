from django.db import models
from django.utils import timezone


class BoastRoast(models.Model):
    boast_or_roast = models.BooleanField(default=True)
    body = models.TextField()
    total_count = models.IntegerField(default=0)
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.body
