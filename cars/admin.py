from django.contrib import admin
from django.utils.html import format_html

from .models import Car


@admin.register(Car)
class CarModelAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html(f"<img src='{object.car_photo.url}' width='50' />")

    thumbnail.short_description = 'Car Image'

    list_display = ['id', 'thumbnail', 'title', 'price', 'model', 'year', 'is_featured']
    search_fields = ['title', 'slug', 'condition', 'description', 'model']
    list_filter = ['state', 'city', 'year', 'is_featured', 'created_date']
    date_hierarchy = 'created'
    list_display_links = ['id', 'title', 'thumbnail']
