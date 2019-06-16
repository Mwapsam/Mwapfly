"""Mwapfly URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from profiles import views as profile_views
from contact import views as contact_views
from checkout import views as checkout_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', profile_views.home, name='home'),
    path('about/', profile_views.about, name='about'),
    path('profiles/', profile_views.userProfile, name='profile'),
    path('checkout/', checkout_views.checkout, name='checkout'),
    path('contact/', contact_views.contact, name='contact'),
    path('accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
