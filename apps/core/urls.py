from django.urls import path

from apps.core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('request/', views.donation_request_create, name='request'),
    path('donate/', views.donate, name='donate'),
    path('request-delete/<int:drequest_id>/', views.donation_request_delete),

]
