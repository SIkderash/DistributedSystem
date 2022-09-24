from datetime import datetime
from django.db import models

# Create your models here.
class Stories(models.Model):
    uid = models.CharField(primary_key=True, max_length=100)
    username = models.CharField(max_length=100)
    time = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.uid

class Status(models.Model):
    uid = models.CharField(primary_key=True, max_length=100)
    username = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)
    time = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.uid