from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, MessageForm
from django.contrib import messages


# Create your views here.
@login_required(login_url='login')
def home(request):
    form = MessageForm()        # Creates a message form

    if request.method == "POST":
        form = MessageForm(request.POST)

        if form.is_valid():
            form.instance.sender = request.user
            form.save()
            form = MessageForm()
            messages.success(request, 'Message sent!!')
    context = {
        'form': form
    }
    return render(request, 'home.html', context)

def register_page(request):
    form = RegisterForm()       # Creates a user registration form

    # Collect the data from user
    if request.method == "POST":
        form = RegisterForm(request.POST)

        # If data is vaild as per requirement then the user is registered successfully
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created Successfully!!')
            return redirect('login')
        
    context = {
        'form': form
    }
    return render(request, 'register.html', context)

def login_page(request):
    # collect username and password
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # autheticate user with the credentials and return user object if correct credentials
        user = authenticate(request, username=username, password=password)

        # checks whether user is in database
        if user is not None:
            login(request, user)
            return redirect('home')           
        else:
            messages.error(request, 'Please Check your username or password!!')

    context = {}
    return render(request, 'login.html', context)

def logout_page(request):
    logout(request)
    return redirect('login')