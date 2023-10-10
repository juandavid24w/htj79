from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from member.forms import (
    UserCreationForm,
)


@require_http_methods(["GET", "POST"])
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
