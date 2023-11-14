from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import SignUpForm
from .models import Record
def home(request):
    records = Record.objects.all()
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
        return render(request, 'home.html', {'records': records})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been Logged out..")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
    return render(request, 'register.html', {'form':form})

def customer_record(request, pk):
    if request.user.is_authenticated:
        cus = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':cus})
    else:
        messages.success("You must Logged In!")
        return redirect('home')


def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, f"You Have Successfully delete Record {pk}")
        return redirect('home')
    else:
        messages.success("You must Logged In!")
        return redirect('home')