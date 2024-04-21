import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
def landing(request):
    artist = Artist.objects.all()
    return render(request, 'landing/landing.html', {'date': datetime.now(), 'artists': artist})