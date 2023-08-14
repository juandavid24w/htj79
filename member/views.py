from django.shortcuts import render
from member.forms import UserCreationForm, ProfileCompletionForm, PaymentForm
from member.models import Members
from django.contrib.auth.hashers import make_password

# Create your views here.


def userCreation(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.password = make_password(form.data.get('password'))
            if request.POST.get('news'):
                pass
            return render(request,
                          template_name='step1.html',
                          context={'form': form})
    else:
        return render(request,
                      template_name='step1.html',
                      context={'form': UserCreationForm})
