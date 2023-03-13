from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Message(models.Model):
    content = models.TextField()
    time_sent = models.DateTimeField(auto_now_add=True)
    sender = models.OneToOneField(User, on_delete=models.CASCADE)