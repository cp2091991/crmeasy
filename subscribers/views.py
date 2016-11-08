from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .models import Subscriber
from .forms import SubscriberForm
def search(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            s_query = form.cleaned_data['search_query']
            s_results = SomeTable.objects.filter(name=s_query)
            return render(request, 'search.html', {'form': form, 's_results': s_results})
    else:
        form = SearchForm()

    return render(request, 'search.html', {'form': form,})
def subscriber_new(request, template='subscribers/subscriber_new.html'):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            # Unpack form values
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            # Create the User record
            user = User(username=username, email=email,
                        first_name=first_name, last_name=last_name)
            # Create the User record
            user = User(username=username, email=email)
            user.set_password(password)
            user.save()
            address_one = form.cleaned_data['address_one']
            address_two = form.cleaned_data['address_two']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            sub = Subscriber(address_one=address_one, address_two=address_two,
                             city=city, state=state, user_rec=user)
            sub.save()
            # Create Subscriber Record
            # Process payment (via Stripe)
            # Auto login the user
            return HttpResponseRedirect('/success/')
    else:
        form = SubscriberForm()

    return render(request, template, {'form':form})
