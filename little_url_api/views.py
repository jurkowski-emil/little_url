import string
import random

from django.http.request import HttpRequest

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Url


@api_view(['POST'])
def get_or_generate_short_url(request: HttpRequest) -> Response:
    try:
        _url_entry = Url.objects.get(long=request.data['url'])
        _short_url_response = _url_entry.short
    except Url.DoesNotExist:
        _short_url_response = "http://localhost:8000/" + ''.join(random.sample(string.ascii_lowercase, 6))
        Url.objects.create(
            long=request.data['url'],
            short=_short_url_response
        )

    return Response({'url': _short_url_response})


@api_view(['POST'])
def retrieve_long_url(request: HttpRequest) -> Response:
    try:
        _url_entry = Url.objects.get(short=request.data['url'])
        _long_url_response = _url_entry.long
    except Url.DoesNotExist:
        _long_url_response = None
    return Response({'url': _long_url_response})

