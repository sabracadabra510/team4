from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from apps.core.models import DonationRequest
from django import forms

class AddDonationRequestForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    cover_url = forms.URLField(max_length=127)
    quantity = forms.CharField(max_length=3)

# Two example views. Change or delete as necessary.
def home(request):

    context = {
        'example_context_variable': 'Change me.',
    }

    return render(request, 'pages/home.html', context)

def about(request):
    context = {
    }

    return render(request, 'pages/about.html', context)

# def request(request):
#     context = {
#     }

#     return render(request, 'pages/request.html', context)

def donation_request_create(request):
    if request.method == 'POST':
        form = AddDonationRequestForm(request.POST)
        if form.is_valid():
            #logged_in_user = request.user
            # print('Current user:', logged_in_user)

            DonationRequest.objects.create(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                #creator_user=logged_in_user,
            )
            return redirect('/')
    else:
        # if a GET  we'll create a blank form
        form = AddDonationRequestForm()
    context = {
        'form': form,
    }
    return render(request, 'pages/request.html', context)
