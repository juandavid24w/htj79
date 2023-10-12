from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, resolve_url
from django.views import View
from django.http import HttpResponse
from django.views.decorators.http import require_GET, require_POST, require_safe
from member.forms import LoginForm


class SignInView(View):
    form_class = LoginForm
    template_name = "_base.html"

    def get(self, request):
        return render(
            request, template_name=self.template_name, context={"form": self.form_class}
        )

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                return redirect(resolve_url("home"))
        return render(
            request,
            template_name=self.template_name,
            context={"form": self.form_class, "error": "email/password."},
        )

    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse("method is not allowed", status=405)


@require_GET
def signout(request):
    logout(request)
    return redirect(resolve_url("home"))
