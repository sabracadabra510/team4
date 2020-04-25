from django.db import models

# Create your models here.

class DonationRequest(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    cover_url = models.URLField(max_length=127)
    quantity = models.CharField(max_length=3)
    destination = models.CharField(max_length= 50)

class Donors(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)

