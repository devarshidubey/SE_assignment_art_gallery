from rest_framework import serializers
from .models import *

class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = (
            "company_name",
            "address"
        )

class ArtTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtType
        fields = (
            "name",
        )

class ArtSerializer1(serializers.ModelSerializer):
    art_type = ArtTypeSerializer()
    class Meta:
        model = Art
        fields = (
            "name",
            "art_type",
            "prize"
        )

class ArtistSerializer(serializers.ModelSerializer):
    sponsors = SponsorSerializer(many = True)
    exhibition = ArtSerializer1(many = True)
    class Meta:
        model = Artist
        fields = (
            "name",
            "sponsors",
            "exhibition"
        )

class ArtistSerializer1(serializers.ModelSerializer):
    sponsors = SponsorSerializer(many = True)
    class Meta:
        model = Artist
        fields = (
            "name",
            "sponsors",
        )

class ArtSerializer(serializers.ModelSerializer):
    art_type = ArtTypeSerializer()
    artist = ArtistSerializer1(read_only = True)
    class Meta:
        model = Art
        fields = (
            "name",
            "art_type",
            "artist",
            "prize",
        )