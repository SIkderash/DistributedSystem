

# Create your models here.
from datetime import datetime
from django.db import models

# Create your models here.
class Stories(models.Model):
    uid = models.CharField(primary_key=True, max_length=100)
    username = models.CharField(max_length=100)
    time = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.uid


# Create your models here.
class EncodedImages(models.Model):
    uid = models.CharField(primary_key=True, max_length=100)
    
    def __str__(self):
        return self.uid