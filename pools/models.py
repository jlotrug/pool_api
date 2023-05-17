from django.db import models
from django.conf import settings

class League(models.Model):
    league_name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.league_name

class Pool(models.Model):
    pool_name = models.CharField(max_length=50, blank=False)
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    winner = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.pool_name
    
class Game(models.Model):
    # Made team names can be null so game can be created and then updated
    team_one = models.CharField(max_length=50, blank=True, null=True)
    team_two = models.CharField(max_length=50, blank=True, null=True)
    winner = models.CharField(max_length=50, blank=True, null=True)
    pool = models.ForeignKey(Pool, on_delete=models.CASCADE)

class Pick(models.Model):
    choice = models.CharField(max_length=50, blank=True)
    correct = models.BooleanField(default=False)
    game = models.ForeignKey(Game, on_delete = models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class GameCard(models.Model):
    wins = models.IntegerField(default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pool = models.ForeignKey(Pool, on_delete=models.CASCADE)
    


