"""
URL configuration for example project.
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from exemple import views as exemple_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", exemple_views.home, name="home"),
    path("hx/get-country/", exemple_views.hx_get_country, name="hx-get-country"),
    path("__debug__/", include("debug_toolbar.urls")),
]
