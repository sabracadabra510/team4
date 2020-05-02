from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from apps.core.models import DonationRequest
from django import forms
import requests
    
class AddDonationRequestForm(forms.ModelForm):
    class Meta:
        model = DonationRequest
        fields = ['title',  'quantity', 'info']


def home(request):
    logged_in_user = request.user
    context = {
    }
    return render(request, 'pages/home.html', context)

def about(request):
    context = {
    }

    return render(request, 'pages/about.html', context)

#Donate page - the listing of requested books
def donate(request):
    donation_requests = DonationRequest.objects.all()

    context = {
        'donation_requests': donation_requests,
    }

    return render(request, 'pages/donate.html', context)

#Donations request page - with the form for making a book request
@login_required
def donation_request_create(request):
    donation_requests = DonationRequest.objects.all()
    if request.method == 'POST':
        form = AddDonationRequestForm(request.POST)
        if form.is_valid():
            #finally solve thanks to this video: https://www.youtube.com/watch?v=zJWhizYFKP0
            ############################################################
            title = form.cleaned_data['title']
            response = requests.get(f'http://openlibrary.org/search.json?title={title}&limit=1')
            data = response.json()
            if data['num_found'] > 0:
                cover_id = data['docs'][0]['cover_i']
                url = f'http://covers.openlibrary.org/b/id/{cover_id}-M.jpg'
            else:
                url = ''
            print('hello' + title)
            ############################################################
            instance = form.save(commit=False)
            instance.creator_user = request.user
            instance.cover_url = url
            instance.save()

            return redirect('/request/')
    else:
        # if a GET create a blank form
        form = AddDonationRequestForm()
    context = {
        'donation_requests': donation_requests,
        'form': form,
    }
    return render(request, 'pages/request.html', context)

#the logged in user / request maker can delete the request they make
@login_required
def donation_request_delete(request, drequest_id):
    # DELETE reading list from database
    donation_request = DonationRequest.objects.get(id=drequest_id)

    # BONUS: Security
    if donation_request.creator_user == request.user:
        donation_request.delete()

    return redirect('/request/')