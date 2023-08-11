from django.shortcuts import render
from member.forms import UserCreationForm, ProfileCompletionForm, PaymentForm
# from django.contrib.auth.hashers import make_password

# Create your views here.


def userCreation(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print(request.POST.get('news'))
            return render(request,
                          template_name='step1.html',
                          context={'form': form})
    else:
        return render(request,
                      template_name='step1.html',
                      context={'form': UserCreationForm})
