"""
URL configuration for webgame project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path("home", views.homepage, name='home'),
    path("my-pets", views.pets, name='my-pets'),
    path("add", views.addPet, name='add'),
    path("fight", views.homepage, name='fight'),
    path("hatchery", views.hatcher, name='hatch'),
    path("", views.toHome),
    path("logout", views.logout_view, name='logout'),
    path("login", views.login_view, name='login'),
    path("register", views.register_view, name='register'),
    path("settings", views.settings, name='settings'),
    path('settingspost', views.settings_post, name='settings_post'),
    path('determine-gender/<int:egg_id>/', views.determine_gender, name='determine-gender'),
    path('hatch-egg/<int:egg_id>/', views.hatch_egg, name='hatch-egg'),
    path('breed', views.breed_pets, name='breed'),
    path('wibblywobbly', views.timeskip, name='timeskip')
    # path('admin-breed', views.aBreed, name='admin-breed')
]
