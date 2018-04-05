from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,'landing.html')


def profile(request):



    return render(request,'profile.html')
# Create your views here.
