from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'car_id', 'user_id', 'created']
    list_filter = ['customer_needs', 'created', 'updated']
    search_fields = ['customer_needs', 'email', ]
    list_display_links = ['id', 'first_name', ]
    list_per_page = 100