from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

def home(request):
    dict = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "You have been Logged In!")
            return redirect('home')
        else:
            messages.success(request, "There are was an error Try again...!")
            return redirect('home')
    else:
        return render(request, 'home.html', dict)

def login_user(request):
    pass

def logout_user(request):
    pass