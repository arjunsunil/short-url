from rest_framework.serializers import ModelSerializer
from shorten_url.models import ShortURL

class ShortURLSerializer(ModelSerializer):
    class Meta:
        model=ShortURL
        fields='__all__'
        extra_kwargs = {'short_url': {'read_only': True}}