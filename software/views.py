from django.shortcuts import render
from software.models import Category

# Create your views here.


def index(request):
    return render(request, "alternatives.html", {"categories": Category.objects.all()})
