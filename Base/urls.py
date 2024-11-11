from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Home.views import Home_view
from About.views import About_view
from Contact.views import Contact_view

urlpatterns = [
    path('', Home_view, name='base_view'),
    path('admin/', admin.site.urls),  
    path('About/', About_view, name='about_view'),
    path('Contact/', Contact_view, name='contact_view'),
    path('Blog/', include('Blog.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
