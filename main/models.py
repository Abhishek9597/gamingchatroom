from django.db import models
# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=120)
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=10)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Message(models.Model):
    content = models.TextField()
    time_sent = models.DateTimeField(auto_now_add=True)
    sender = models.OneToOneField(User, on_delete=models.CASCADE)