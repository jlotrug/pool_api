from django.db import models
from django.contrib.auth.models import AbstractUser
from pools.models import League, UserLeague

class CustomUser(AbstractUser):
    first_name = models.CharField(null=True, blank=True, max_length=100)
    last_name = models.CharField(null=True, blank=True, max_length=100)
    wins = models.IntegerField(default=0)
    leagues = models.ManyToManyField(League, through='pools.UserLeague')
