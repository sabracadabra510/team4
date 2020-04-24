from django.db import models

# Create your models here.

class DonationRequest(models.Model):
    username = models.CharField(max_length=30)
    text = models.CharField(max_length=160)
    created = models.DateTimeField(auto_now_add=True)
