from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),  # Define the URL pattern for the index view
]
