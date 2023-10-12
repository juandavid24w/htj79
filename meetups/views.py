from django.shortcuts import render, resolve_url, redirect
from meetups.forms import MeetupForm
from django.views import View
from django.views.decorators.http import require_GET, require_http_methods
from django.contrib.auth.decorators import login_required
from django.http import Http404
from meetups.models import Meetups


# Meetup Creation
class MeetupCreationView(View):
    def get(self, request):
        return render(request, "create_meetup.html", {"form": MeetupForm})

    def post(self, request):
        form = MeetupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(resolve_url("meetups_list"))

        else:
            errors = form.errors
            print(form.data)
            return render(
                request, "create_meetup.html", {"form": form, "errors": errors}
            )


# Listing the meetups by user login


@require_GET
def events(request):
    meetups = Meetups.objects.all()
    context = {"meetups": meetups}
    return render(request, "meetup_forms.html", context)

    # if request.user.is_authenticated:
    #     return render(
    #         request, template_name="meetup_forms.html", context={"form": MeetupForm}
    #     )
    # else:
    #     return redirect(resolve_url("home"))


class MeetupView(View):
    template_name = "meetup_detail.html"

    def user_is_meetup_owner(self, user, meetup_id):
        meetup = get_object_or_404(Meetup, pk=meetup_id)
        return meetup.owner == user

    @login_required
    @require_http_methods(["GET", "POST"])
    def edit(self, request, meetup_id):
        if not self.user_is_meetup_owner(request.user, meetup_id):
            raise Http404

        meetup = get_object_or_404(Meetup, pk=meetup_id)

        if request.method == "POST":
            form = MeetupForm(request.POST, request.FILES, instance=meetup)
            if form.is_valid():
                form.save()
                return redirect("meetup_list")
        else:
            form = MeetupForm(instance=meetup)
        return render(request, self.template_name, {"form": form, "meetup": meetup})

    @login_required
    @require_http_methods(["GET", "POST"])
    def delete(self, request, meetup_id):
        if not self.user_is_meetup_owner(request.user, meetup_id):
            raise Http404

        meetup = get_object_or_404(Meetup, pk=meetup_id)

        if request.method == "POST":
            meetup.delete()
            return redirect("meetup_list")
        return render(request, "delete_meetup.html", {"meetup": meetup})
