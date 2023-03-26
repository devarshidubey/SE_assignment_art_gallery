from django.urls import path
from .views import *

urlpatterns = [
    path("arts", ArtListView.as_view(), name = "art-list"),
    path("arts/<int:id>", ArtDetailView.as_view(), name = "art-detail"),
    path("artists", ArtistListView.as_view(), name = "artist-list"),
    path("artists/<int:id>", ArtistDetailView.as_view(), name = "artist-detail"),
]