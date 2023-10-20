from django.urls import path
from meetups import views

urlpatterns = [
    path("list/", views.events, name="meetups_list"),
    path("create_meetups/", views.MeetupCreationView.as_view(), name="meetups_create"),
    path("edit/<int:meetup_id>/", views.MeetupEditView.as_view(), name="meetups_edit"),
]
