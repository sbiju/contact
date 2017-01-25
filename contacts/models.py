from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


def upload_location(instance, filename):
    return '%s, %s' %(instance.first_name, filename)


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=80,blank=True, null=True)
    last_name = models.CharField(max_length=80, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    photo = models.FileField(upload_to=upload_location, blank=True, null=True)
    house = models.CharField(verbose_name='House No/Name', max_length=120, blank=True, null=True)
    street = models.CharField(verbose_name='Street', max_length=120, blank=True, null=True)
    city = models.CharField(max_length=120, blank=True, null=True)
    state = models.CharField(max_length=120, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return str(self.user)


class Contact(models.Model):
    first_name = models.CharField(max_length=80,blank=True, null=True)
    last_name = models.CharField(max_length=80, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    photo = models.FileField(upload_to=upload_location, blank=True, null=True)
    house = models.CharField(verbose_name='House No/Name', max_length=120, blank=True, null=True)
    street = models.CharField(verbose_name='Street', max_length=120, blank=True, null=True)
    city = models.CharField(max_length=120, blank=True, null=True)
    state = models.CharField(max_length=120, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return str(self.first_name)