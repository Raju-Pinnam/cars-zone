from datetime import datetime

from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse

from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField

from .utils import (STATE_CHOICES, YEAR_CHOICES,
                    features_choices, door_choices,
                    gen_item_slug, car_image_saver)


class Car(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256, unique=True, blank=True)
    state = models.CharField(max_length=32, choices=STATE_CHOICES)
    city = models.CharField(max_length=128)
    color = models.CharField(max_length=64)
    model = models.CharField(max_length=128)
    year = models.IntegerField(choices=YEAR_CHOICES)
    condition = models.CharField(max_length=64)
    price = models.IntegerField()
    description = RichTextField()
    car_photo = models.ImageField('Main Image', upload_to=car_image_saver)
    car_photo_1 = models.ImageField(upload_to=car_image_saver, blank=True)
    car_photo_2 = models.ImageField(upload_to=car_image_saver, blank=True)
    car_photo_3 = models.ImageField(upload_to=car_image_saver, blank=True)
    car_photo_4 = models.ImageField(upload_to=car_image_saver, blank=True)
    features = MultiSelectField(max_length=254, choices=features_choices)
    body_style = models.CharField(max_length=128)
    engine = models.CharField(max_length=256)
    transmission = models.CharField(max_length=256)
    interior = models.CharField(max_length=256)
    miles = models.IntegerField()
    doors = models.CharField(max_length=32, choices=door_choices)
    passengers = models.IntegerField()
    vin_no = models.CharField(max_length=128)
    milage = models.IntegerField()
    fuel_type = models.CharField(max_length=64)
    no_of_owners = models.CharField(max_length=64)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now(), blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('cars:detail', args=[self.slug])


def post_save_slug_func(sender, instance, *args, **kwargs):
    if instance.slug is None or instance.slug == '':
        print("Is coming Here")
        instance.slug = gen_item_slug(instance)


pre_save.connect(post_save_slug_func, sender=Car)
