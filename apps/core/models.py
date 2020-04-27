from django.db import models
from apps.accounts.models import User

# Create your models here.

class DonationRequest(models.Model):
    title = models.CharField(max_length=127)
    info = models.TextField()
    cover_url = models.URLField(max_length=127, blank=True)
    quantity = models.IntegerField(default=0)
    creator_user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True) # Add current date
