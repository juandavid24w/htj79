from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.validators import ValidationError
from member.models import Members, ProofOfPayment
from member.forms import (
    UserCreationForm,
)
from member.serializers import UserSerializer


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


# API Views


# Accounts
class CreateUserView(ModelViewSet):
    queryset = Members.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    pagination_class = None

    def get_queryset(self):
        queryset = super().get_queryset().filter(id=self.request.user.id)
        return queryset


class ProofOfPaymentView(ModelViewSet):
    queryset = ProofOfPayment.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = None

    def get_queryset(self):
        queryset = super().get_queryset().filter(id=self.request.user)
        return queryset
