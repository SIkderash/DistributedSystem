from django.db import models

# Create your models here.

class Users(models.Model):
    uid = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    isVerified = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username