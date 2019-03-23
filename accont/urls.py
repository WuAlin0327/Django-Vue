from django.contrib import admin
from django.urls import path,include
from django.views.generic.base import TemplateView
from accont import views

urlpatterns = [
    path('login/',views.LoginView.as_view())
]
