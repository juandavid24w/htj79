from django.shortcuts import render, resolve_url, redirect, get_object_or_404
from meetups.forms import MeetupForm
from django.views import View
from django.views.decorators.http import require_GET, require_http_methods
from django.contrib.auth.decorators import login_required, permission_required
from django.http import Http404, HttpResponse, HttpResponseRedirect
from meetups.models import Meetups
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from uuid import uuid4


# Meetup Creation
class MeetupCreationView(View):
    def get(self, request):
        return render(request, "create_meetup.html", {"form": MeetupForm})

    def post(self, request):
        form = MeetupForm(request.POST, request.FILES)
        if form.is_valid():
            meetup = form.save(commit=False)
            meetup.id = uuid4()
            meetup.author = request.user  # assigns the created used as owner
            meetup.save()
            return redirect(resolve_url("meetups_list"))

        else:
            errors = form.errors
            print(errors)
            print(form.data)
            return render(
                request, "create_meetup.html", {"form": form, "errors": errors}
            )


# Listing the meetups by user login
@require_GET
def events(request):
    return render(request, "meetup_list.html", {"meetups": Meetups.objects.all()})


@method_decorator(login_required, name="get")
class MeetupEditView(View):
    def get(self, request, meetup_id):
        meetup = get_object_or_404(Meetups, pk=meetup_id)

        if meetup.author == request.user:
            form = MeetupForm(instance=meetup)
            return render(request, "meetup_edit.html", {"form": form, "meetup": meetup})
        else:
            return HttpResponse("You are not the owner of this meetup.")

    def post(self, request, meetup_id):
        meetup = get_object_or_404(Meetups, id=meetup_id)

        if "delete" in request.POST:  # Check if the "Delete" button was clicked
            if meetup.author == request.user:
                meetup.delete()
                return HttpResponseRedirect(reverse("meetups_list"))
            else:
                return HttpResponse("You are not the owner of this meetup.")

        if meetup.author == request.user:
            form = MeetupForm(request.POST, request.FILES, instance=meetup)

            if form.is_valid():
                form.save()
                return redirect("meetups_list")

        else:
            return HttpResponse("You are not the owner of this meetup.")

        return HttpResponse("An error occurred while updating the meetup.")


# def delete(request, meetup_id):
#     if not self.user_is_meetup_owner(request.user, meetup_id):
#         raise Http404

#     meetup = get_object_or_404(Meetup, pk=meetup_id)

#     if request.method == "POST":
#         meetup.delete()
#         return redirect("meetup_list")
#     return render(request, "meetup_delete.html", {"meetup": meetup})


class MeetupDetailView(View):
    def get(self, request, slug):
        meetup = Meetups.objects.get(slug=slug)
        context = {"meetup": meetup}
        return render(request, "meetup_details.html", context)
