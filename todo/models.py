from django.db import models

# Create your models here.

from django.utils import timezone

class assignment(models.Model):
    task = models.CharField(max_length=50)
    date_and_time = models.DateTimeField(default=timezone.now())
    breakfast = models.BooleanField(default=False)
    def __str__(self):
        return self.task
