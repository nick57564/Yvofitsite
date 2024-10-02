from django.contrib import admin
from django.urls import path
from Home.views import Home_view
from About.views import About_view

urlpatterns = [
    path('', Home_view, name='base_view'),
    path('About/', About_view, name='about_view'),
]