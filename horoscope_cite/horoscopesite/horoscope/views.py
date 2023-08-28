from django.shortcuts import render
from django.http import HttpResponse

from .models import Horoscope
# Create your views here.
def index(request):
    return render(request,'horoscope/index.html')

def aqua(request):

    return render(request, 'horoscope/aqua.html')