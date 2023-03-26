from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import *
from .serializers import *

# Test case for the Art model
class ArtModelTestCase(TestCase):
    def setUp(self):
        self.art_type = ArtType.objects.create(name="Painting")
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )
        self.sponsor = Sponsor.objects.create(
            company_name='Test Sponsor',
            address='123 Test St'
        )
        self.artist = Artist.objects.create(name="Bob Ross", user = self.user)
        self.artist.sponsors.add(self.sponsor)
        self.art = Art.objects.create(
            name="Happy Little Trees",
            art_type=self.art_type,
            artist=self.artist,
            prize=1000,
        )

    def test_art_model(self):
        art = Art.objects.get(id=self.art.id)
        self.assertEqual(art.name, "Happy Little Trees")
        self.assertEqual(art.art_type, self.art_type)
        self.assertEqual(art.artist, self.artist)
        self.assertEqual(art.prize, 1000)


# Test case for the Art API
class ArtAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.art_type = ArtType.objects.create(name="Painting")
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )
        self.sponsor = Sponsor.objects.create(
            company_name='Test Sponsor',
            address='123 Test St'
        )
        self.artist = Artist.objects.create(name="Bob Ross", user = self.user)
        self.artist.sponsors.add(self.sponsor)

        self.art = Art.objects.create(
            name="Happy Little Trees",
            art_type=self.art_type,
            artist=self.artist,
            prize=1000,
        )
        self.url = reverse("art-detail", kwargs={"id": self.art.id})

    def test_get_art_list(self):
        response = self.client.get(reverse("art-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_art_detail(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Happy Little Trees")

class ArtistAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.sponsor = Sponsor.objects.create(company_name='Test Sponsor', address='123 Test St.')
        self.artist = Artist.objects.create(name='Test Artist', user=self.user)
        self.artist.sponsors.add(self.sponsor)
        self.url = reverse('artist-list')

    def test_get_artist_list(self):
        response = self.client.get(self.url, format='json')
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_artist_detail(self):
        detail_url = reverse('artist-detail', args=[self.artist.id])
        response = self.client.get(detail_url, format='json')
        serializer = ArtistSerializer(self.artist)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)