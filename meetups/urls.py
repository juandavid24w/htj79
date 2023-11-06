from django.urls import path
from meetups import views

urlpatterns = [
    path("", views.events, name="meetups_list"),
    path("create_meetups/", views.MeetupCreationView.as_view(), name="meetups_create"),
    path("edit/<str:slug>/", views.MeetupEditView.as_view(), name="meetups_edit"),
    path("details/<str:slug>/", views.MeetupDetailView.as_view(), name="meetup_details"),
]

