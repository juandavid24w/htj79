from django.urls import path
from member import views

urlpatterns = [
    path("signup/", views.UserCreationView.as_view(), name="signup"),
]
