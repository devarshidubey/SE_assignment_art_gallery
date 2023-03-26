from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from django.http import Http404

class ArtListView(APIView):

    def get(self, request):
        queryset = Art.objects.all()
        serializer = ArtSerializer(queryset, many = True)
        return Response(serializer.data)
    
class ArtDetailView(APIView):

    def get_object(self, id):
        try:
            return Art.objects.get(id = id)
        except Art.DoesNotExist:
            raise Http404

    def get(self, request, id):
        queryset = self.get_object(id)
        serializer = ArtSerializer(queryset)
        return Response(serializer.data)

class ArtistListView(APIView):

    def get(self, request):
        queryset = Artist.objects.all()
        serializer = ArtistSerializer(queryset, many = True)
        return Response(serializer.data)
    
class ArtistDetailView(APIView):

    def get_object(self, id):
        try:
            return Artist.objects.get(id = id)
        except Artist.DoesNotExist:
            raise Http404

    def get(self, request, id):
        queryset = self.get_object(id)
        serializer = ArtistSerializer(queryset)
        return Response(serializer.data)