from django.shortcuts import render


def cars_list(request):
    return render(request, 'cars/cars_list.html')