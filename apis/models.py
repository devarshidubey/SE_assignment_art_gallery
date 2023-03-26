from django.db import models
from django.contrib.auth.models import User

class Sponsor(models.Model):
    company_name = models.CharField(max_length = 50)
    address = models.CharField(max_length = 128)

    def __str__(self):
        return self.company_name


class ArtType(models.Model):
    name = models.CharField(max_length = 30)
    
    def __str__(self):
        return self.name

class Artist(models.Model):
    name = models.CharField(max_length = 50)
    user = models.OneToOneField(
        User,
        on_delete = models.CASCADE
    )
    sponsors = models.ManyToManyField(
        Sponsor,
        related_name = "artists"
    )
    def __str__(self):
        return self.name


class Art(models.Model):
    name = models.CharField(max_length = 30)
    art_type = models.ForeignKey(
        ArtType,
        on_delete = models.DO_NOTHING
    )
    artist = models.ForeignKey(
        Artist,
        related_name = "exhibition",
        on_delete = models.DO_NOTHING
    )
    prize = models.IntegerField()

    def __str__(self):
        return self.name
