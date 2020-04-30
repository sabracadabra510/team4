from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from apps.core.models import DonationRequest, Donated_books
from django import forms
import os
import requests
os.environ['MAILGUN_API_KEY'] = 'e0b614d21f527201b6faa52154b385fe-f135b0f1-8df4136b'
api_key = os.environ["MAILGUN_API_KEY"]
    
class AddDonationRequestForm(forms.ModelForm):
    class Meta:
        model = DonationRequest
        fields = ['title',  'quantity', 'info']

class Donornameform(forms.ModelForm):
    class Meta:
        model = Donated_books
        fields = ['donor_name']

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
    donation_requests = DonationRequest.objects.all()#extracts all records in donationrequest
    donation_form = Donornameform() #grab name of donor


    context = {
        'donation_requests': donation_requests,
        'donation_form' : donation_form,
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
                        ############################################################
            # Bonus Challenge 4
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

def donate_this_book(request):


    #list of donation requests
    #Short for donate
    if request.method == 'POST':
        form = Donornameform(request.POST)
        if form.is_valid():
           
            name = request.POST.get('donor_name', False)
            request_id = request.POST.get('id', False)
            
            my_instance = DonationRequest.objects.get(id=request_id)

            
            instance = form.save(commit=False) #puts stop to save it
            instance.donation_request = my_instance
            instance.save()
            email = my_instance.creator_user.email
            message = "I'm insterested in donating this book to you"
            # sending email
            try:
                requests.post(
		        "https://api.mailgun.net/v3/sandbox87de3aadc08a409194d029876425a36f.mailgun.org/messages",
		        auth=("api", api_key),
		        data={"from": "Interested Donor <mailgun@sandboxe11fc3e25d97421aa9ae24a95cd2fdc6.mailgun.org>",
			        "to": [email],
			        "subject": my_instance.title,
			        "text": message}),
                #update the donation request to donated
                my_instance.donated_or_not = "<a class=\"btn btn-success btn-md\" role=\"button\">Donated</a>"
                my_instance.save()
                return redirect('donate')
            except:
                print('There was an error sending the email')

                return render(request, '404.html')

        else:
            return render(request, '404.html')

    else:
        # if a GET  we'll create a blank form
        form = Donornameform()
    context = {
        
        'form': form,
    }
    return render(request, 'pages/donate.html', context)

    