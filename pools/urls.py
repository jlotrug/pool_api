from django.urls import path, include
from .views import PoolList, PoolDetail, LeagueList, GameList, GameDetail, PickDetail,PickList, PickCheckRetrieve, UserLeagues, PlayerList, PoolUserCreate, GameCardList
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("dj-rest-auth/", include("dj_rest_auth.urls")),
    path("dj-rest-auth/registration/", include("dj_rest_auth.registration.urls")),
    path("pools/<int:pk>/", PoolDetail.as_view(), name="pool_detail"),
    path("pools/", PoolList.as_view(), name="pool_list"),
    path("games/", GameList.as_view(), name="game_list"),
    path("games/<int:pk>/", GameDetail.as_view(), name="game_detail"),
    path("leagues/", LeagueList.as_view(), name='league_list'),
    path("userleagues/", UserLeagues.as_view(), name='user_leagues'),
    path("pick-check/", PickCheckRetrieve.as_view(), name = "pick-check"),
    path("picks/<int:pk>/", PickDetail.as_view(), name="pick_detail"),
    path("picks/", PickList.as_view(), name="pick_list"),
    path("players/", PlayerList.as_view(), name="player_list"),
    path("pooluser/", PoolUserCreate.as_view(), name="pooluser_create"),
    path("gamecards/", GameCardList.as_view(), name="game_card_list"),
]