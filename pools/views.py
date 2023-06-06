from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics

from .models import Pool, Pick, Game, League, UserLeague, PoolUser
from accounts.models import CustomUser
from accounts.serializers import UserDetailsSerializer
from .permissions import IsAuthorOrReadOnly
from .serializers import PoolSerializer, LeagueSerializer, GameSerializer, PickSerializer, PoolUserSerializer

from rest_framework_simplejwt.views import TokenObtainPairView

class PlayerList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = UserDetailsSerializer

    def get_queryset(self):
        pool_id = self.request.query_params['poolid']
        pool = Pool.objects.get(id=pool_id)

        return pool.players

class PoolList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    

    def get_queryset(self):
        # print(self.request.query_params['leagueid'])
        if 'leagueid' in self.request.query_params:
            searchLeague  = self.request.query_params['leagueid']
            queryset = Pool.objects.filter(league = searchLeague)
        else:
            searchLeague  = self.request.query_params['leaguecode']
            league = League.objects.get(code=searchLeague)
            if len(UserLeague.objects.filter(league=league, user=self.request.user)) < 1:
                UserLeague.objects.create(league=league, user=self.request.user)  
            queryset = Pool.objects.filter(league = league)
        return queryset
    
    serializer_class = PoolSerializer


class PoolDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Pool.objects.all()
    serializer_class = PoolSerializer

class UserLeagues(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = LeagueSerializer

    def get_queryset(self):
        return self.request.user.leagues

class LeagueList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    
    def get_queryset(self):
        user = self.request.user
        queryset = League.objects.filter(user=user)
        return queryset

    serializer_class = LeagueSerializer

class LeagueDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = League.objects.all()
    serializer_class = LeagueSerializer

class GameList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)

    def get_queryset(self, *args, **kwargs):
        if(self.request.query_params.get('poolid', False)):
            searchPool  = self.request.query_params['poolid']
            return Game.objects.filter(pool = searchPool)
        else:
            return Game.objects.all()

    # permission_classes = (IsAuthorOrReadOnly,)
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class PoolUserCreate(generics.CreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = PoolUserSerializer

    def create(self, request, *args, **kwargs):
        if len(PoolUser.objects.filter(pool=request.data['pool'], user=self.request.user)) < 1:
            return super().create(request, *args, **kwargs)
        else:
            return HttpResponse()

class PickList(generics.ListCreateAPIView):

    # def create(self, request, *args, **kwargs):
    #     game_id = request.data['game']
    #     game = Game.objects.get(id=game_id)
    #     pool = game.pool
    #     if len(PoolUser.objects.filter(pool=pool, user=self.request.user)) < 1:
    #         PoolUser.objects.create(pool=pool, user=self.request.user)  

    #     return super().create(request, *args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        if(self.request.query_params.get('game', False)):
            searchPick = self.request.query_params['game']

            # These two are different if the user requesting them is not the author
            # It will send back but we need to notify React that they can't edit it
            # Probably don't want to block it completely though
            print(Pick.objects.filter(game = searchPick)[0].user)
            print(self.request.user)

            return Pick.objects.filter(game = searchPick)
            
        else:
            return Pick.objects.all()

    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Pick.objects.all()
    serializer_class = PickSerializer

class PickDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = PickSerializer
    queryset = Pick.objects.all()


class PickCheckRetrieve(generics.ListAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = PickSerializer
    

    def get_queryset(self, *args, **kwargs):
        print("Reach Query")
        print(self.request.query_params)
        if(self.request.query_params.get('game', False)):
            searchPick = self.request.query_params['game']
            if self.request.query_params.get('player', False):
                searchUser = self.request.query_params['player']
                return Pick.objects.filter(game=searchPick, user=searchUser)
            if Pick.objects.filter(game = searchPick, user=self.request.user).exists():
                return Pick.objects.filter(game = searchPick, user=self.request.user)

    queryset = Game.objects.all()