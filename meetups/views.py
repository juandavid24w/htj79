from django.shortcuts import render, resolve_url, redirect
from meetups.forms import *

# Create your views here.
def events(request):
    if request.user.is_authenticated:
        return render(request, template_name='meetup_forms.html', context={'form': MeetupForm})
    else:
        return redirect(resolve_url('home'))

def create_meetup(request):
    if request.method == 'POST':
        form = MeetupForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('meetup_list')  # Redirect to the list view after successful creation
    else:
        return render(request, 'create_meetup.html', {'form': MeetupForm})