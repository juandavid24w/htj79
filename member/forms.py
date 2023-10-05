from django import forms
from django.core import validators
from django.contrib.auth.forms import password_validation
from member.models import Members, Membership
from glug.models import GLUG
from institutions.models import Institutions
from hacktivist.models import Occupation, EducationalQualification


class LoginForm(forms.Form):
    '''
    Hacktivist Login Form
    module: member.forms.LoginForm
    fields: email, password, remember_me
    '''
    email = forms.EmailField(
        label='',
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'name@glug.org',
        }))
    password = forms.CharField(
        label='',
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': '••••••••',
        }))
    remember_me = forms.BooleanField(
        label='',
        required=False,
        widget=forms.CheckboxInput(attrs={
            'aria-describedby': 'remember',
        }))


class UserCreationForm(forms.ModelForm):
    '''
    Hacktivist User Creation Form
    module: member.forms.UserCreationForm
    fields: first_name, last_name, username, email, contact, password, confirm_password, is_accept_TC
    '''
    first_name = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(
            attrs={
                'pattern':
                '[A-Za-z]{1,150}',
                'placeholder':
                'John',
                'class':
                'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
            }))
    last_name = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(
            attrs={
                'pattern':
                '[A-Za-z]{1,150}',
                'placeholder':
                'Doe',
                'class':
                'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
            }))
    username = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':
                'rounded-none rounded-r-lg bg-gray-50 border border-gray-300 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 min-w-0 w-full text-sm p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
                'placeholder': 'johndoe'
            }))
    email = forms.EmailField(
        label='',
        required=True,
        widget=forms.EmailInput(
            attrs={
                'placeholder':
                'name@glug.org',
                'class':
                'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
            }))
    contact = forms.CharField(
        label='',
        required=True,
        validators=[
            validators.MinLengthValidator(10),
            validators.MaxLengthValidator(10)
        ],
        widget=forms.NumberInput(
            attrs={
                'min':
                '0',
                'placeholder':
                '9876543210',
                'class':
                'rounded-none rounded-r-lg bg-gray-50 border border-gray-300 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 min-w-0 w-full text-sm p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
            }))
    password = forms.CharField(
        label='',
        required=True,
        validators=[password_validation.validate_password],
        widget=forms.PasswordInput(
            attrs={
                'data-popover-target':
                'popover-password',
                'data-popover-placement':
                'bottom',
                'placeholder':
                '••••••••',
                'class':
                'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
            }))
    confirm_password = forms.CharField(
        label='',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':
                '••••••••',
                'class':
                'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
            }))
    is_accept_TC: 'Is User Accept the Terms & Conditions' = forms.BooleanField(
        label='',
        required=True,
        widget=forms.CheckboxInput(
            attrs={
                'class':
                'w-4 h-4 bg-gray-50 rounded border-gray-300 focus:ring-3 focus:ring-blue-300 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:bg-gray-700 dark:border-gray-600'
            }))

    class Meta:
        model = Members
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'contact',
            'password',
            'is_accept_TC',
        ]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            self.add_error('password', "Password doesn't match")


class ProfileCompletionForm(forms.ModelForm):
    glug = forms.ModelChoiceField(
        label='',
        required=True,
        queryset=GLUG.objects.all(),
        widget=forms.Select(
            attrs={
                'class':
                'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
            }))
    institute = forms.ModelChoiceField(
        label='',
        required=True,
        queryset=Institutions.objects.all(),
        widget=forms.Select(
            attrs={
                'class':
                'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
            }))
    occupation = forms.ChoiceField(
        label='',
        required=True,
        choices=Occupation.choices,
        widget=forms.Select(
            attrs={
                'class':
                'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
            }))
    edu_qualification = forms.CharField(
        label='',
        required=True,
        widget=forms.Select(
            choices=EducationalQualification.choices,
            attrs={
                'class':
                'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
            }))

    class Meta:
        model = Members
        fields = [
            'glug',
            'institute',
            'occupation',
            'edu_qualification',
        ]


class MembershipForm(forms.ModelForm):
    payment_method = forms.CharField(
        label='',
        required=True,
        widget=forms.Select(choices=Membership.PAYMENT_METHOD_CHOICES))

    class Meta:
        model = Membership
        fields = [
            'payment_method',
        ]


class PaymentForm(forms.Form):
    transaction_id = forms.IntegerField(
        label='',
        required=True,
        widget=forms.NumberInput(
            attrs={
                'class':
                'rounded-lg bg-gray-50 border border-gray-300 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 min-w-0 w-full text-sm p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
            }))


class ResetPasswordForm(forms.Form):
    pass
