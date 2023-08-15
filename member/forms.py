from django import forms
from member.models import Members
from glug.models import GLUG
from institutions.models import Institutions
from hacktivist.models import Occupation, EducationalQualification


class LoginForm(forms.Form):
    email = forms.EmailField(
        label='',
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class':
                'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-gray-600 focus:border-gray-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
                'placeholder': 'name@glug.org',
            }))
    password = forms.CharField(
        label='',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class':
                'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-gray-600 focus:border-gray-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
                'placeholder': '••••••••',
            }))
    remember_me = forms.BooleanField(
        label='',
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'class':
                'w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-gray-300 dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-gray-600 dark:ring-offset-gray-800',
                'aria-describedby': 'remember',
            }))


class UserCreationForm(forms.ModelForm):
    first_name = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(
            attrs={
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
    contact = forms.IntegerField(
        label='',
        required=True,
        widget=forms.NumberInput(
            attrs={
                'placeholder':
                '9876543210',
                'class':
                'rounded-none rounded-r-lg bg-gray-50 border border-gray-300 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 min-w-0 w-full text-sm p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
            }))
    password = forms.CharField(
        label='',
        required=True,
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
    is_accept_TC = forms.BooleanField(
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
            'confirm_password',
            'is_accept_TC',
        ]


class ProfileCompletionForm(forms.Form):
    glug = forms.ModelChoiceField(
        label='',
        required=True,
        queryset=GLUG.objects.all(),
        widget=forms.Select(
            attrs={
                'class':
                'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
            }))
    institution = forms.ModelChoiceField(
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
    # address = forms.CharField(
    #     label='',
    #     required=True,
    #     widget=forms.Textarea(
    #         attrs={
    #             'rows':
    #             '7',
    #             'class':
    #             "block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
    #             'placeholder':
    #             "House.No, Street, Nagar, Area, District, State, Country - Pincode"
    #         }))


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
