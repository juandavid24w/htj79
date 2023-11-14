from django.urls import path
from software import views

urlpatterns = [
    path('', views.index, name="software_home"),
    # path('<slug:slug>', views.index, name="software")
]
