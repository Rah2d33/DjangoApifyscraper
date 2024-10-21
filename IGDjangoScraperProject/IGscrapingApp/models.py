# C:\WebScapingPOCs\Apify\IGDgangoScraper\IGDjangoScraper\IGDjangoScraperProject\IGscrapingApp\models.py

# models.py

from django.db import models

class InstagramProfile(models.Model):
    username = models.CharField(max_length=255, unique=True)
    display_name = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    profile_url = models.URLField(blank=True)

    def __str__(self):
        return self.username
