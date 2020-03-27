from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import BoastRoast
from .serializers import BoastRoastSerializer

class BoastRoastViewSet(viewsets.ModelViewSet):
    queryset = BoastRoast.objects.all()
    serializer_class = BoastRoastSerializer

    @action(detail=True, methods=['get'])
    def upvote(self, request, pk=None):
        upvotes = BoastRoast.objects.get(pk=pk)
        upvotes.total_count += 1
        upvotes.save()
        return Response({'status': 'upvoted!'})

    @action(detail=True, methods=['get'])
    def downvote(self, request, pk=None):
        downvote = BoastRoast.objects.get(pk=pk)
        downvote.total_count -= 1
        downvote.save()
        return Response({'status': 'downvoted!'})