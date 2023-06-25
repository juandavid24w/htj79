from django.shortcuts import render
from member.forms import UserCreationForm, PaymentForm
# Create your views here.


def userCreation(request):
    form = PaymentForm()
    return render(request, template_name='step4.html', context={'form': form})
