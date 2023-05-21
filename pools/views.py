from django.shortcuts import render
from rest_framework import generics

from .models import Pool, Pick, Game, League
# from .permissions import IsAuthorOrReadOnly
from .serializers import PoolSerializer

from rest_framework_simplejwt.views import TokenObtainPairView

class PoolList(generics.ListCreateAPIView):
    # permission_classes = (IsAuthorOrReadOnly,)
    print("Hello Pools")
    queryset = Pool.objects.all()
    serializer_class = PoolSerializer


class PoolDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthorOrReadOnly,)
    queryset = Pool.objects.all()
    serializer_class = PoolSerializer