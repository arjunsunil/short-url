"""django models file to handle database tables"""
from random import choices
from string import ascii_letters
from django.db import models

from django.conf import settings


class ShortURL(models.Model):
    """shortURL django model"""
    url = models.URLField()
    short_url = models.URLField(max_length=50, blank=True,null=True)
    created_time = models.DateTimeField(auto_now_add=True)


    def shortener(self):
        """shortener url logic"""
        while True:
            random_string = ''.join(choices(ascii_letters,k=6))
            new_url=settings.DOMAIN + '/' + random_string

            if not ShortURL.objects.filter(short_url=new_url).exists():
                break

        return new_url

    def save(self,*args, **kwargs):
        if not self.short_url:
            new_url = self.shortener()
            self.short_url = new_url
        return super().save(*args, **kwargs)
