from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from apps.core.models import DonationRequest
from django import forms
import requests
import os
os.environ['MAILGUN_API_KEY'] = '40f84bf16437f27c107717bf55c5d184-f135b0f1-eb8810fd'
api_key= os.environ['MAILGUN_API_KEY']


class AddDonationRequestForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
   # cover_url = forms.URLField(max_length=127)
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
              #  cover_url=form.cleaned_data['description'],
                quantity=form.cleaned_data['description'],
                #creator_user=logged_in_user,
            )
            return redirect('/request/')
    else:
        # if a GET  we'll create a blank form
        form = AddDonationRequestForm()
    context = {
        'form': form,
    }
    return render(request, 'pages/request.html', context)

def email_send(request):
    return render(request, 'send_email.html')


def send_email(request):
    
    name = request.POST.get('name', False),
    email = request.POST.get('email', False),
    message_text = request.POST.get('message', False),
    print(message_text)
    # phone_number = request.POST.get('phone_number', False),
    # print(phone_number)
    # message = "phone number : " + phone_number[0] + "text:" + message_text[0]

    try:
        requests.post(
		"https://api.mailgun.net/v3/sandboxe11fc3e25d97421aa9ae24a95cd2fdc6.mailgun.org/messages",
		auth=("api", api_key),
		data={"from": "Excited User <mailgun@sandboxe11fc3e25d97421aa9ae24a95cd2fdc6.mailgun.org>",
			"to": [email],
			"subject": name,
			"text": message_text})
        return render(request, "send_email.html")
    except:
        print('hi')

        return render(request, "send_email.html")