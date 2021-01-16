from datetime import datetime
from django.shortcuts import render

from teams.models import Team
from cars.models import Car


def home(request):
    teams = Team.objects.all().order_by('created')
    cars = Car.objects.order_by('-created_date')
    # search_fields = Car.objects.values('title', 'model', 'city', 'state', 'year', 'body_style')
    model_fields = Car.objects.values_list('model', flat=True).distinct()
    city_fields = Car.objects.values_list('city', flat=True).distinct()
    body_style_fields = Car.objects.values_list('body_style', flat=True).distinct()
    context = {
        'teams': teams,
        'cars': cars,
        'model_fields': model_fields,
        'city_fields': city_fields,
        'body_style_fields': body_style_fields,
        'year_range': range(2000, (datetime.now().year + 1)),
    }
    return render(request, 'pages/home.html', context)


def about(request):
    teams = Team.objects.all().order_by('created')
    context = {
        'teams': teams
    }
    return render(request, 'pages/about.html', context)


def service(request):
    return render(request, 'pages/service.html')


def contact(request):
    return render(request, 'pages/contact.html')
