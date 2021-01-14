from django.db import models


class Team(models.Model):
    first_name = models.CharField(max_length=127)
    last_name = models.CharField(max_length=127)
    designation = models.CharField(max_length=127)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    facebook_link = models.URLField(max_length=255, blank=True)
    twitter_link = models.URLField(max_length=255, blank=True)
    google_plus_link = models.URLField(max_length=255, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ['-created']
