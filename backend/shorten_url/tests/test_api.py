import json
from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from shorten_url.models import ShortURL
from shorten_url.serializers import ShortURLSerializer


class GetURLTestCase(TestCase):
    def setUp(self):
        url = "https://github.com/TierMobility/frontend-challenge/tree/feat/fullstack-challange#coding-challenge-"
        short_url = ShortURL(
            url=url
        )
        short_url.save()

    def test_get_list(self):
        """GET the list page of shorturl."""
        # get API response
        response = self.client.get(reverse('shorturl-list'))
        # get data from db
        short_urls = ShortURL.objects.all()
        serializer = ShortURLSerializer(short_urls, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreateURLTestCase(TestCase):
    def setUp(self):
        self.payload = {
            "url" :"https://github.com/TierMobility/frontend-challenge/tree/feat/fullstack-challange#coding-challenge-"
        }

    def test_create_shorturl(self):
        """create a shorturl"""
        response = self.client.post(
            reverse('shorturl-list'),
            data=json.dumps(self.payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

