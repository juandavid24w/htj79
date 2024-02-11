from django.urls import path
from rest_framework.routers import DefaultRouter
from member import views

app_name = "member"

router = DefaultRouter()
router.register("api/signup", views.CreateUserView)
router.urls

urlpatterns = router.urls + [
    path("signup/", views.UserCreationView.as_view(), name="signup"),
]
