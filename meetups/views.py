from django.shortcuts import render, resolve_url, redirect
from meetups.forms import *

# Create your views here.
def demo(request):
    if request.user.is_authenticated:
        return render(request, template_name='meetup_forms.html', context={'form': MeetupRegistrationForm})
    else:
        return redirect(resolve_url('home'))