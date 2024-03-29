from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
# from django.contrib.auth import get_user_model
from .models import Pool, Game, Pick, League, PoolUser, GameCard
# from accounts.models import CustomUser


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['first_name'] = user.first_name

        return token
    
class PoolSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "pool_name",
            "league",
        )
        model = Pool

    def update(self, instance, validated_data):
        print(instance.league)
        return super().update(instance, validated_data)

class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "league_name",
            "user",
            "code",
        )
        model = League

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "team_one",
            "team_two",
            "winner",
            "pool",
        )
        model = Game

class PickSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "user",
            "choice",
            "correct", 
            "game",
        )
        model = Pick

class PoolUserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "user",
            "pool"
        )
        model = PoolUser

class GameCardSerializer(serializers.ModelSerializer):
    player_first_name = serializers.CharField(source='user.first_name')
    player_last_name = serializers.CharField(source='user.last_name')
    class Meta:
        fields = (
            "id",
            "wins",
            "user",
            "pool",
            "player_first_name",
            "player_last_name",
        )
        model = GameCard