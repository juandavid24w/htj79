from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import password_validation
from django.shortcuts import render
from member.models import Members
from member.forms import UserCreationForm, ProfileCompletionForm, PaymentForm


# Create your views here.
def userCreation(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        try:
            password_validation.validate_password(form.data.get('password'))
        except ValidationError as errors:
            return render(request,
                          template_name='step1.html',
                          context={
                              'form': form,
                              'errors': errors.messages,
                          })
        if form.is_valid():
            obj = form.save(commit=False)
            obj.password = make_password(form.data.get('password'))
            print(obj.is_accept_TC)
            if request.POST.get('news'):
                obj.is_news_subscribed = True
            # obj.save()
            return render(request,
                          template_name='step1.html',
                          context={'form': form})
    else:
        return render(request,
                      template_name='step1.html',
                      context={'form': UserCreationForm})
