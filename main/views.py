from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.contrib import messages

# Create your views here.
@login_required(login_url='login')
def home(request):
    context = {}
    return render(request, 'home.html', context)

def register_page(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
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
            messages.error(request, 'Wrong Info')

    context = {}
    return render(request, 'login.html', context)

def logout_page(request):
    logout(request)
    return redirect('login')