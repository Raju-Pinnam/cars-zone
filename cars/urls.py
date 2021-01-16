from django.urls import path
from . import views

app_name = 'cars'

urlpatterns = [
    path('', views.cars_list, name='list'),
    path('<slug:slug>/', views.car_detail, name='detail'),
]
