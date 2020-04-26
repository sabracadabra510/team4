from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from apps.core.models import DonationRequest
from django import forms

    
class AddDonationRequestForm(forms.ModelForm):
    class Meta:
        model = DonationRequest
        fields = ['title',  'quantity', 'description']



# Two example views. Change or delete as necessary.
def home(request):
    logged_in_user = request.user
    print('Current user:', logged_in_user)

    context = {
        'example_context_variable': 'Change me.',
    }

    return render(request, 'pages/home.html', context)

def about(request):
    context = {
    }

    return render(request, 'pages/about.html', context)

def donate(request):
    donation_requests = DonationRequest.objects.all()

    context = {
        'donation_requests': donation_requests,
    }

    return render(request, 'pages/donate.html', context)

# def request(request):
#     context = {
#     }

#     return render(request, 'pages/request.html', context)
@login_required
def donation_request_create(request):
    donation_requests = DonationRequest.objects.all()
    if request.method == 'POST':
        form = AddDonationRequestForm(request.POST)
        if form.is_valid():
            # logged_in_user = request.user
            # print('Current user:', logged_in_user)
            #finally solve thanks to this video: https://www.youtube.com/watch?v=zJWhizYFKP0
            instance = form.save(commit=False)
            instance.creator_user = request.user
            instance.save()

            return redirect('/request/')
    else:
        # if a GET  we'll create a blank form
        form = AddDonationRequestForm()
    context = {
        'donation_requests': donation_requests,
        'form': form,
    }
    return render(request, 'pages/request.html', context)

@login_required
def donation_request_delete(request, drequest_id):
    # D in CRUD --- DELETE reading list from database
    donation_request = DonationRequest.objects.get(id=drequest_id)

    # BONUS: Security
    if donation_request.creator_user == request.user:
        donation_request.delete()

    return redirect('/request/')