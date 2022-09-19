from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Hello, Django!")

def simulation(request):
    return render(
        request,
        'first_page.html'
    )