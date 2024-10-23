# IGscrapingApp/views.py

from django.core.cache import cache
from django.shortcuts import render
from .instagram_scraper import get_combined_instagram_data
from django.views.decorators.cache import never_cache

@never_cache
def index(request):
    scraped_data = None

    # Check if the clear action was triggered
    if request.method == 'GET' and 'clear' in request.GET:
        # Clear any scraped data
        request.session.flush()  # Clear session data or reset scraped_data
    elif request.method == 'GET' and 'display_name' in request.GET:
        username = request.GET.get('display_name')
        # Fetch the Instagram profile data
        scraped_data = get_combined_instagram_data(username)

    return render(request, 'index.html', {'scraped_data': scraped_data})

