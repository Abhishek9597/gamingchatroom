from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Message
from django.forms import ModelForm

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2',
        ]

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = [
            'content',
        ]