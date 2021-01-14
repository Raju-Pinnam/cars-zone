from django.contrib import admin
from django.utils.html import format_html

from .models import Team


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        if object.photo:
            return format_html(f"<img src={object.photo.url} width='40' />")
        return "No Image"

    thumbnail.short_description = "Image"

    list_display = ['id', 'thumbnail', '__str__', 'designation', 'created', 'updated']
    list_filter = ['created', 'updated']
    search_fields = ['first_name', 'last_name', 'designation', ]
    date_hierarchy = 'created'
    list_display_links = ['id', 'thumbnail', '__str__']
