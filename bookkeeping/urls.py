from django.contrib import admin
from django.urls import path,include
from django.views.generic.base import TemplateView
from bookkeeping import views

urlpatterns = [
    path('charge/',views.ChargeAPIView.as_view())
]
