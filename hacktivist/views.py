from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, resolve_url
from member.models import Members
from member.forms import LoginForm


def signin(request):
    if request.user.is_authenticated:
        return render(request, template_name='_base.html')
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password')
                try:
                    user = Members.objects.get(email=email)
                except Members.DoesNotExist:
                    user = None
                if user:
                    user = authenticate(request,
                                        username=user.username,
                                        password=password)
                    if user is not None:
                        login(request, user)
                        return redirect('/')
            return render(request,
                          template_name='_base.html',
                          context={
                              'form': LoginForm,
                              'error': 'email/password.'
                          })
        else:
            return render(request,
                          template_name='_base.html',
                          context={'form': LoginForm})


def signout(request):
    logout(request)
    return redirect(resolve_url('signin'))