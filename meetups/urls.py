from django.urls import path
from meetups import views

urlpatterns = [
    path('events/', views.events, name='events'),
    path('create_meetups/', views.create_meetup, name='create_meetups'),]
