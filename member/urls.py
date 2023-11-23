from django.urls import path
from member import views

app_name = "member"

urlpatterns = [
    path("signup/", views.UserCreationView.as_view(), name="signup"),
]
