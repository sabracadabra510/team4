from django.urls import path

from apps.core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('request/', views.donation_request_create, name='request'),
    path('send_email', views.send_email, name='send_email')
]
