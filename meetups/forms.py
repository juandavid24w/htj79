from django import forms
from django.forms import Form, ModelForm, DateField, widgets
from django.core import validators
from glug.models import GLUG
from hacktivist.models import Locations
from meetups.models import Meetups


class MeetupForm(forms.ModelForm):
    location = forms.ModelChoiceField(
        queryset=Locations.objects.all(),
        widget=forms.Select(),
    )
    glug = forms.ModelChoiceField(
        label="",
        required=True,
        queryset=GLUG.objects.all(),
        widget=forms.Select(),
    )
    date = forms.DateField(
        widget=widgets.DateInput(attrs={"type": "date"}),
    )
    time = forms.TimeField(widget=widgets.TimeInput(attrs={"type": "time"}))
    description = forms.CharField()
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
            "poster",
        ]
