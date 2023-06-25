from django.urls import path
from member import views

urlpatterns = [
    path('signup/', views.userCreation, name='signup'),
]
