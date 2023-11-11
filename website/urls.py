"""Defines URL patterns for learning_logs."""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
]
