from django.urls import path
from . import views

urlpatterns = [
    path('', views.account, name='account'),
    path('purchase_history/<purchase_number>', views.purchase_history, name='purchase_history'),
]