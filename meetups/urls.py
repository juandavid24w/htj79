from django.urls import path
from meetups import views

urlpatterns = [
    path('demo/', views.demo, name='demo'),
]
