"""Схемы URL для users"""

from django.urls import path, include
from . import views

app_name = "users"

urlpatterns=[
    # URL authorization by default
    path("", include('django.contrib.auth.urls')),
    path("register/", views.register, name="register")
]