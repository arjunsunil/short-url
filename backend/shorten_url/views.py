"""django views file to handle request response cylce"""
from rest_framework import viewsets
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.decorators import api_view

from shorten_url import serializers
from shorten_url.models import ShortURL

class ShortURLViewSet(viewsets.ModelViewSet):
    """Handle creating and updating shortURL"""
    serializer_class = serializers.ShortURLSerializer
    queryset = ShortURL.objects.all()
    lookup_field = 'short_url'


@api_view(['POST'])
def get_specific_url(request):
    try:
        if 'short_url' not in request.data:
            raise APIException("Please provide the short_url field")
        short_url = request.data.get('short_url', None)
        url_obj = ShortURL.objects.get(short_url=short_url)
        original_url = url_obj.url
    except:
        raise APIException("Short url does not exist")
    return Response({"original_url" : original_url})