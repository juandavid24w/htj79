from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.decorators.http import require_GET, require_POST, require_safe
from member.forms import (
    UserCreationForm,
)


class UserCreationView(View):
    form_class = UserCreationForm
    template_name = "signup/userCreate.html"

    def get(self, request):
        return render(
            request,
            template_name=self.template_name,
            context={"form": self.form_class},
        )

    def post(self, request):
        form = self.form_class(request.POST)
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
                template_name=self.template_name,
                context={
                    "form": form,
                    "errors": form.errors,
                },
            )

    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse("method is not allowed", status=405)
