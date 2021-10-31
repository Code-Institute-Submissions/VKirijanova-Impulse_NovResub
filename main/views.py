from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view to return the index page """

    return render(request, 'main/index.html')


def cluboverview(request):
    return render(request, 'main/cluboverview.html')


def timetable(request):
    return render(request, 'main/timetable.html')


def facilities(request):
    return render(request, 'main/facilities.html')