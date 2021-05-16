from django.shortcuts import render
from django.http import HttpResponse
from .models import Services

# Create your views here.
def hi(request):
    all_services = Services.objects.all
    return render(request, 'INVAPP/home.html',{all:all_services})
