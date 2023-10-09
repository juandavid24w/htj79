from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from hacktivist.models import Subscription
from member.forms import (
    UserCreationForm,
    ProfileCompletionForm,
    PaymentForm,
    MembershipForm,
)
from datetime import date


# Create your views here.
# def userCreation(request):
#     if request.user.is_authenticated:
#         user = request.user
#         if user.profile_status == 1:  # Profile info
#             if request.method == 'POST':
#                 form = ProfileCompletionForm(request.POST, instance=user)
#                 print(request.POST)
#                 if form.is_valid():
#                     obj = form.save(commit=False)
#                     obj.profile_status = 2
#                     if request.POST.get('address'):
#                         obj.address = request.POST.get('address')
#                     obj.save()
#                     return redirect(resolve_url('signup'))
#                 else:
#                     return render(request,
#                                   template_name='step2.html',
#                                   context={
#                                       'form': form,
#                                       'errors': form.errors,
#                                   })
#             else:
#                 return render(request,
#                               template_name='step2.html',
#                               context={'form': ProfileCompletionForm})
#         elif user.profile_status == 2:  # Membership
#             if request.method == 'POST':
#                 form = MembershipForm(request.POST, instance=user)
#                 print(request.POST)
#                 if form.is_valid():
#                     obj = form.save(commit=False)
#                     print(obj)
#                     return redirect(resolve_url('signup'))
#                 else:
#                     return render(request,
#                                   template_name='step3.html',
#                                   context={
#                                       'form': form,
#                                       'errors': form.errors,
#                                   })
#             else:
#                 subscription = Subscription.objects.filter(
#                     occupation__contains=[user.occupation]).first()
#                 return render(request,
#                               template_name='step3.html',
#                               context={
#                                   'form': MembershipForm,
#                                   'subscription': subscription
#                               })
#         elif user.profile_status == 3:  # payment proof
#             if request.method == 'POST':
#                 pass
#             else:
#                 return render(request,
#                               template_name='step4.html',
#                               context={'form': ''})
#     else:
#         if request.method == 'POST':
#             form = UserCreationForm(request.POST)
#             if form.is_valid():
#                 obj = form.save(commit=False)
#                 obj.password = make_password(form.data.get('password'))
#                 if request.POST.get('news'):
#                     obj.is_news_subscribed = True
#                 obj.save()
#                 return redirect(resolve_url('home'))
#             else:
#                 return render(request,
#                               template_name='step1.html',
#                               context={
#                                   'form': form,
#                                   'errors': form.errors,
#                               })
#         else:
#             return render(request,
#                           template_name='step1.html',
#                           context={'form': UserCreationForm})


def userCreation(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.password = make_password(form.data.get("password"))
            if request.POST.get("news"):
                obj.is_news_subscribed = True
            obj.save()
            return redirect(resolve_url("home"))
        else:
            return render(
                request,
                template_name="signup/step1.html",
                context={
                    "form": form,
                    "errors": form.errors,
                },
            )
    else:
        return render(
            request,
            template_name="signup/step1.html",
            context={"form": UserCreationForm},
        )
