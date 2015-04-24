from django.shortcuts import render
from traffic.models import *
# Create your views here.
def index(request):
    return render(request, 'traffic/show.html')