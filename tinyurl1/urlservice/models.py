from __future__ import unicode_literals

from django.db import models
# Django actually creates a User model as part of the auth module
from django.contrib.auth.models import User

# Create your models here.
class Tinyurl(models.Model):
    user = models.ForeignKey(User)
    long_url = models.CharField(max_length=100)
    short_url = models.CharField(max_length=100)

#class User(models.Model):
#    username = models.CharField(max_length=30)
#    password = models.CharField(max_length=30)
