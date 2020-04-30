from django.contrib import admin
from .models import DonationRequest
from .models import Donated_books

# Register your models here.
admin.site.register(DonationRequest)
admin.site.register(Donated_books)