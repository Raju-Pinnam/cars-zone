from django.shortcuts import render
from teams.models import Team


def home(request):
    teams = Team.objects.all().order_by('created')
    context = {
        'teams': teams
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
