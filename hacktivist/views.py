from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, resolve_url
from member.forms import LoginForm


def signin(request):
    if request.user.is_authenticated:
        if request.user.profile_status in [4, 5]:
            return render(request, template_name='_base.html')
        else:
            return redirect(resolve_url('signup'))
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password')
                user = authenticate(request, email=email, password=password)
                if user is not None:
                    login(request, user)
                    return redirect(resolve_url('home'))
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
    return redirect(resolve_url('home'))