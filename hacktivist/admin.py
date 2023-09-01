from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.utils.translation import gettext_lazy as _
from django import forms
from leaflet.admin import LeafletGeoAdminMixin
from hacktivist.models import Locations, Subscription, Occupation


class LocationAdmin(LeafletGeoAdmin):
    list_display = [
        'district',
        'latitude',
        'longitude',
    ]


class CheckboxSelectMultipleAsCharField(forms.CheckboxSelectMultiple):

    def format_value(self, value):
        if value is not None and isinstance(value, str):
            value = list(value)
        return super().format_value(value)


class MultipleChoiceFieldAsCharField(forms.MultipleChoiceField):
    widget = CheckboxSelectMultipleAsCharField

    def to_python(self, value):
        return ''.join(super().to_python(value))

    def validate(self, value):
        super().validate(value)
        if len(value) > len(self.choices):
            raise ValidationError('Too many choices.')


class SubscriptionAdminForm(forms.ModelForm):
    occupation = MultipleChoiceFieldAsCharField(
        choices=Occupation.choices,
        widget=FilteredSelectMultiple(verbose_name=_('Occupation'),
                                      is_stacked=False))

    class Meta:
        model = Subscription
        fields = '__all__'


class SubscriptionAdmin(admin.ModelAdmin):
    form = SubscriptionAdminForm
    list_display = [
        'name',
        'price',
    ]
    readonly_fields = [
        'created_at',
        'updated_at',
    ]


admin.site.register(Locations, LocationAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
