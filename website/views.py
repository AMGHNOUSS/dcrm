from django.shortcuts import render

def home(request):
    """The home page for Learning Log."""
    return render(request, 'home.html')
