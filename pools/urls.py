from django.urls import path, include
from .views import PoolList, PoolDetail
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
]