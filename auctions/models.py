from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    name = models.CharField(max_length=20)
    image = models.CharField(max_length=64)
    price = models.IntegerField(default=1)
    desc = models.CharField(max_length=100, default="No Description")

    highestBid = models.IntegerField(default=1)
