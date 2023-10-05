from django import forms
from django.core import validators
from glug.models import GLUG
from hacktivist.models import Locations
from meetups.models import Meetups

class MeetupForm(forms.ModelForm):
    location = forms.ModelChoiceField(queryset=Locations.objects.all())
    glug = forms.ModelChoiceField(queryset=GLUG.objects.all())
    class Meta:
        model= Meetups
        fields=['location', 'glug', 'date', 'time', 'platform', 'venue', 'description', 'minutes', 'poster']