from django.urls import include, path

urlpatterns = [
    path('little_url_api/', include('little_url_api.urls'))
]
