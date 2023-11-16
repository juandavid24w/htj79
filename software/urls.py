from django.urls import path
from software import views

app_name = "software"

urlpatterns = [
    path("", views.index, name="home"),
    path("tags/<slug:slug>/", views.index, name="tag"),
    path("categories/<slug:slug>/", views.index, name="category"),
    path("<slug:slug>/", views.index, name="software"),
]
