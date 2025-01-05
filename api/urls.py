from django.contrib import admin
from django.urls import path
from .api import api
from ui import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
    path("", views.index),
]
