from django import forms
from django.forms import Form, ModelForm, DateField, widgets
from django.core import validators
from glug.models import GLUG
from hacktivist.models import Locations
from meetups.models import Meetups

class MeetupForm(forms.ModelForm):
    location = forms.ModelChoiceField(
        queryset=Locations.objects.all(),
        label= 'Location',
        help_text='Select the location where the meetup will take place.'
    )
    glug = forms.ModelChoiceField(
            label="",
            required=True,
            queryset=GLUG.objects.all(),
            widget=forms.Select(
                attrs={
                    "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                }
            )
        )
    date = forms.DateField( 
            widget=widgets.DateInput(attrs={'type': 'date'}),
        )
    time = forms.TimeField()
    minutes= forms.TextInput(
        attrs={"class":"text-white font-medium rounded-lg text-base px-5 py-3 w-full sm:w-auto text-center bg-blue-700"}
    )
    class Meta:
        model= Meetups
        fields=['location','glug', 'date', 'time', 'mode', 'venue', 'description', 'minutes', 'poster']