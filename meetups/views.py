from django.shortcuts import render, resolve_url, redirect
from meetups.forms import MeetupForm
from django.views import View
from django.views.decorators.http import require_GET


# Create your views here.
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


@require_GET
def events(request):
    if request.user.is_authenticated:
        return render(
            request, template_name="meetup_forms.html", context={"form": MeetupForm}
        )
    else:
        return redirect(resolve_url("home"))


# def createMeetup(request):
#     if request.method == "POST":
#         form = MeetupForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect(resolve_url("meetups_list"))

#         else:
#             errors = form.errors
#             print(form.data)
#             return render(
#                 request, "create_meetup.html", {"form": form, "errors": errors}
#             )
#     else:
#         return render(request, "create_meetup.html", {"form": MeetupForm})
