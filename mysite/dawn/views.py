from django.shortcuts import render
from django.http import HttpResponse
import dawn.time_and_date_finder as TimeFinder
# Create your views here.


def index(request):
    try:
        return HttpResponse(str(TimeFinder.TimeFinder(request.GET['input'])))
    except:
        return HttpResponse("There no attr")