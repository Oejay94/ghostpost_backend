from django.shortcuts import render
from rest_framework import viewsets

from .models import BoastRoast
from .serializers import BoastRoastSerializer

class BoastRoastViewSet(viewsets.ModelViewSet):
    queryset = BoastRoast.objects.all()
    serializer_class = BoastRoastSerializer