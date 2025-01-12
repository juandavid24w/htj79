from django import forms
from django.core import validators
from django.contrib.auth import password_validation
from member.models import Members, Membership
from glug.models import GLUG
from institutions.models import Institutions
from hacktivist.models import Occupation, EducationalQualification
from django.conf import settings


class LoginForm(forms.Form):
    """
    Hacktivist Login Form
    module: member.forms.LoginForm
    fields: email, password, remember_me
    """

    email = forms.EmailField(
        label="",
        required=True,
        widget=forms.EmailInput(
            attrs={
                "placeholder": settings.PLACEHOLDER["email"],
            }
        ),
    )
    password = forms.CharField(
        label="",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": settings.PLACEHOLDER["password"],
            }
        ),
    )
    remember_me = forms.BooleanField(
        label="",
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "aria-describedby": "remember",
            }
        ),
    )


class UserCreationForm(forms.ModelForm):
    """
    Hacktivist User Creation Form
    module: member.forms.UserCreationForm
    fields: first_name, last_name, username, email, contact, password, confirm_password, is_accept_TC
    """

    first_name = forms.CharField(
        label="",
        required=True,
        widget=forms.TextInput(
            attrs={
                "pattern": "[A-Za-z]{1,150}",
                "placeholder": settings.PLACEHOLDER["firstName"],
                "title": "First name should only contain letters.",
                "class": "invalid:[&:not(:placeholder-shown):not(:focus)]:border-red-500",
            }
        ),
    )
    last_name = forms.CharField(
        label="",
        required=True,
        widget=forms.TextInput(
            attrs={
                "pattern": "[A-Za-z]{1,150}",
                "placeholder": settings.PLACEHOLDER["lastName"],
                "title": "Last name should only contain letters.",
                "class": "invalid:[&:not(:placeholder-shown):not(:focus)]:border-red-500",
            }
        ),
    )
    username = forms.CharField(
        label="",
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": settings.PLACEHOLDER["username"],
                "class": "rounded-none rounded-r-md",
            }
        ),
    )
    email = forms.EmailField(
        label="",
        required=True,
        widget=forms.EmailInput(
            attrs={
                "placeholder": settings.PLACEHOLDER["email"],
            }
        ),
    )
    contact = forms.CharField(
        label="",
        required=True,
        validators=[
            validators.MinLengthValidator(10),
            validators.MaxLengthValidator(10),
        ],
        widget=forms.NumberInput(
            attrs={
                "type": "tel",
                "min": "0",
                "placeholder": settings.PLACEHOLDER["tel"],
                "class": "rounded-none rounded-r-md",
            }
        ),
    )
    password = forms.CharField(
        label="",
        required=True,
        validators=[password_validation.validate_password],
        widget=forms.PasswordInput(
            attrs={
                "data-popover-target": "popover-password",
                "data-popover-placement": "bottom",
                "placeholder": settings.PLACEHOLDER["password"],
            }
        ),
    )
    confirm_password = forms.CharField(
        label="",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": settings.PLACEHOLDER["password"],
            }
        ),
    )
    is_accept_TC = forms.BooleanField(
        label="",
        required=True,
        widget=forms.CheckboxInput(attrs={}),
    )

    class Meta:
        model = Members
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "contact",
            "password",
            "is_accept_TC",
        ]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            self.add_error("password", "Password doesn't match")


class ProfileCompletionForm(forms.ModelForm):
    glug = forms.ModelChoiceField(
        label="",
        required=True,
        queryset=GLUG.objects.all(),
        widget=forms.Select(attrs={}),
    )
    institute = forms.ModelChoiceField(
        label="",
        required=True,
        queryset=Institutions.objects.all(),
        widget=forms.Select(attrs={}),
    )
    occupation = forms.ChoiceField(
        label="",
        required=True,
        choices=Occupation.choices,
        widget=forms.Select(attrs={}),
    )
    edu_qualification = forms.CharField(
        label="",
        required=True,
        widget=forms.Select(
            choices=EducationalQualification.choices,
            attrs={},
        ),
    )

    class Meta:
        model = Members
        fields = [
            "glug",
            "institute",
            "occupation",
            "edu_qualification",
        ]


class MembershipForm(forms.ModelForm):
    payment_method = forms.CharField(
        label="",
        required=True,
        widget=forms.Select(choices=Membership.CHOICES_PAYMENT_METHOD),
    )

    class Meta:
        model = Membership
        fields = [
            "payment_method",
        ]


class PaymentForm(forms.Form):
    transaction_id = forms.IntegerField(
        label="",
        required=True,
        widget=forms.NumberInput(attrs={}),
    )


class ResetPasswordForm(forms.Form):
    pass
