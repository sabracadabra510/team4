from django.db import models
from apps.accounts.models import User

# Create your models here.

class DonationRequest(models.Model):
    title = models.CharField(max_length=127)
    info = models.TextField()
    cover_url = models.URLField(max_length=127, blank=True)
    quantity = models.IntegerField(default=0)
    creator_user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    donated_or_not = models.CharField(max_length=200, default = "<a class=\"btn btn-primary btn-md\" role=\"button\">Not Donated</a>")#holds the badge to show if book 
    #is donated or not    
    created = models.DateTimeField(auto_now_add=True) # Add current date
    def __str__(self):
        return self.title
        


# List of donation requests

class Donated_books(models.Model):
    donor_name = models.CharField(max_length= 40)
    donation_request = models.ForeignKey(DonationRequest, default=None, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.donation_request.title #show title of book than the default setting that comes with django in the admin, linked through foreign key


# not_donated = models.CharField(max_length=200, default = " ")
#     yes_donated = models.CharField(max_length=200, default= " ")