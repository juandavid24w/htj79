from django import forms
from django.forms import Form, ModelForm, DateField, widgets
from django.core import validators
from glug.models import GLUG
from hacktivist.models import Locations
from meetups.models import Meetups


class MeetupForm(forms.ModelForm):
    location = forms.ModelChoiceField(
        queryset=Locations.objects.all(),
        widget=forms.Select(
            attrs={
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
            }
        ),
    )
    glug = forms.ModelChoiceField(
        label="",
        required=True,
        queryset=GLUG.objects.all(),
        widget=forms.Select(
            attrs={
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
            }
        ),
    )
    date = forms.DateField(
        widget=widgets.DateInput(
            attrs={
                "type": "date",
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
            }
        ),
    )
    time = forms.TimeField(widget=forms.TimeInput(format="%H:%M"))
    minutes = forms.FileField()
    poster = forms.ImageField()

    class Meta:
        model = Meetups
        fields = [
            "location",
            "glug",
            "date",
            "time",
            "mode",
            "venue",
            "description",
            "minutes",
            "poster",
        ]
