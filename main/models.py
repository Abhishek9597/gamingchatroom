from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Message(models.Model):
    content = models.TextField()
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    time_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content