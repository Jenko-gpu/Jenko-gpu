from django.shortcuts import render
from django.http import HttpResponse
from dawn.models import Note

import dawn.time_and_date_finder as TimeFinder


# Create your views here.


def index(request):
    return render(request, 'main/index.html', {
        'view_answer1': TimeFinder.TimeFinder(request.GET['input']).get_time(),
        'view_answer2': TimeFinder.TimeFinder(request.GET['input']).get_date()
    })
