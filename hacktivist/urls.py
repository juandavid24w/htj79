"""
URL configuration for hacktivist project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from hacktivist import views

# Site Settings
admin.site.site_header = "Hacktivist"
admin.site.site_title = "Hacktivist Portal"
admin.site.index_title = "Welcome to Hacktivist Portal"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", views.SignInView.as_view(), name="home"),
    path("logout/", views.signout, name="signout"),
    path("user/", include("member.urls", namespace="member")),
    path("meetups/", include("meetups.urls")),
    path("alternatives/", include("software.urls", namespace="software")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
