from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from member.forms import UserCreationForm, ProfileCompletionForm, PaymentForm


# Create your views here.
def userCreation(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.password = make_password(form.data.get('password'))
            if request.POST.get('news'):
                obj.is_news_subscribed = True
            obj.save()
            return redirect(resolve_url('home'))
        else:
            return render(request,
                          template_name='step1.html',
                          context={
                              'form': form,
                              'errors': form.errors,
                          })
    else:
        return render(request,
                      template_name='step1.html',
                      context={'form': UserCreationForm})
