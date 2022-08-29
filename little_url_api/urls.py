from django.urls import path
from . import views

urlpatterns = [
    path('short/', views.get_or_generate_short_url),
    path('long/', views.retrieve_long_url)
]
