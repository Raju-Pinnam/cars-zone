from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages

from cars.models import Car

from .models import Contact


def inquiry(request):
    if request.method == "POST":
        car_id = request.POST.get('car_id')
        user_id = request.POST.get('user_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        customer_need = request.POST.get('customer_need')
        car_title = request.POST.get('car_title')
        city = request.POST.get('city')
        phone = request.POST.get('phone')
        state = request.POST.get('state')
        email = request.POST.get('email')
        message = request.POST.get('message')
        car = get_object_or_404(Car, id=car_id)
        try:
            contact = Contact(first_name=first_name, last_name=last_name,
                              car_id=car_id, customer_needs=customer_need, car_title=car_title,
                              city=city, state=state, email=email, phone=phone, comments=message)
            contact.user_id = user_id
            contact.save()
            messages.success(request, "Your query has been submitted")
        except Exception:
            messages.error(request, "Some field is not valid")

        return redirect(car.get_absolute_url())
    return redirect('cars:list')
