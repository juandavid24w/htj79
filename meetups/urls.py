from django.urls import path
from meetups import views

urlpatterns = [
    path("list/", views.events, name="meetups_list"),
    path("create_meetups/", views.create_meetup, name="meetups_create"),
]
