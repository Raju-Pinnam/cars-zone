from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Car


def cars_list(request):
    objects = Car.objects.all()
    paginator = Paginator(objects, 1)
    page = request.GET.get('page')
    try:
        cars = paginator.page(page)
    except PageNotAnInteger:
        cars = paginator.page(1)
    except EmptyPage:
        cars = paginator.page(paginator.num_pages)

    context = {
        'cars': cars,
        'page': page
    }
    return render(request, 'cars/cars_list.html', context)


def car_detail(request, slug):
    car = get_object_or_404(Car, slug=slug)
    context = {
        'car': car
    }
    return render(request, 'cars/car_detail.html', context)
