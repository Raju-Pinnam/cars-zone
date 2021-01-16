from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from datetime import datetime

from .models import Car


def cars_list(request):
    objects = Car.objects.all()
    paginator = Paginator(objects, 1)
    model_fields = Car.objects.values_list('model', flat=True).distinct()
    city_fields = Car.objects.values_list('city', flat=True).distinct()
    body_style_fields = Car.objects.values_list('body_style', flat=True).distinct()
    page = request.GET.get('page')
    try:
        cars = paginator.page(page)
    except PageNotAnInteger:
        cars = paginator.page(1)
    except EmptyPage:
        cars = paginator.page(paginator.num_pages)

    context = {
        'cars': cars,
        'page': page,
        'model_fields': model_fields,
        'city_fields': city_fields,
        'body_style_fields': body_style_fields,
        'year_range': range(2000, (datetime.now().year + 1)),
    }
    return render(request, 'cars/cars_list.html', context)


def car_detail(request, slug):
    car = get_object_or_404(Car, slug=slug)
    context = {
        'car': car
    }
    return render(request, 'cars/car_detail.html', context)


def search_func(request):
    cars = Car.objects.order_by('-created')
    if 'query' in request.GET:
        query = request.GET.get('query')
        if query:
            search_vector = SearchVector('title', 'description')
            search_query = SearchQuery(query)
            cars = cars.annotate(search=search_vector,
                                 rank=SearchRank(search_vector,
                                                 search_query)).filter(search=search_query).order_by('-rank')
    if 'model' in request.GET:
        model = request.GET.get('model')
        if model:
            cars = cars.filter(model__iexact=model)
    if 'city' in request.GET:
        city = request.GET.get('city')
        if city:
            cars = cars.filter(model__iexact=city)
    if 'year' in request.GET:
        year = request.GET.get('year')
        if year:
            cars = cars.filter(model__iexact=year)
    if 'body_type' in request.GET:
        body_type = request.GET.get('body_type')
        if body_type:
            cars = cars.filter(model__iexact=body_type)
    if 'min_price' in request.GET:
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')
        if min_price:
            cars = cars.filter(price__gte=min_price, price__lte=max_price)

    context = {
        'cars': cars
    }
    return render(request, 'cars/search.html', context)
