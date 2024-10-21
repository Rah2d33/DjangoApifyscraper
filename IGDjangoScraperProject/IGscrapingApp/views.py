# IGscrapingApp/views.py

from django.shortcuts import render
from .instagram_scraper import get_combined_instagram_data

def index(request):
    scraped_data = None  # Initialize scraped_data to None

    if request.method == 'GET' and 'username' in request.GET:
        username = request.GET['username']
        
        # Fetch the Instagram profile data
        scraped_data = get_combined_instagram_data(username)

    # Pass the scraped_data to the template context
    return render(request, 'index.html', {'scraped_data': scraped_data})
