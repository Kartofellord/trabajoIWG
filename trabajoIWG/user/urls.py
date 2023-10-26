from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signin', views.signin, name='signin'),
    path('profile', views.profile, name='profile'),
    path('profileSettings', views.profileSettings, name='profileSettings'),
    path('signup', views.signup, name='signup'),
    path('signout', views.signout, name='signout'),
]