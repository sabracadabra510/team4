from django.db import models
from apps.accounts.models import User

# Create your models here.

class DonationRequest(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    cover_url = models.URLField(max_length=127)
    quantity = models.IntegerField(default=0)
    creator_user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)