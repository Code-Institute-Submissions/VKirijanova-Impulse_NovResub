from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('cluboverview', views.cluboverview, name='cluboverview'),
    path('timetable', views.timetable, name='timetable'),
    path('facilities', views.facilities, name='facilities'),
]
