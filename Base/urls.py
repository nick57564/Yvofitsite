from django.contrib import admin
from django.urls import path
from Home.views import Home_view
from About.views import About_view
from Contact.views import Contact_view
from Blog.views import Blog_view

urlpatterns = [
    path('', Home_view, name='base_view'),
    path("admin/", admin.site.urls),
    path('About/', About_view, name='about_view'),
    path('Contact/', Contact_view, name='contact_view'),
    path('Blog/', Blog_view, name='blog_view'),
]