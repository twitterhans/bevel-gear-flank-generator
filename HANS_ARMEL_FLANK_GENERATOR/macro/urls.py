from django.urls import path
from django.contrib import admin
from .views import MacroView

urlpatterns = [
    path("", MacroView.as_view()),
]
