from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    car_id = models.IntegerField()
    customer_needs = models.CharField(max_length=128)
    car_title = models.CharField(max_length=256)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=16)
    email = models.EmailField(max_length=256)
    phone = models.CharField(max_length=16)
    comments = models.TextField(blank=True)
    user_id = models.IntegerField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
