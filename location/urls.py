# Description: This file contains the URL patterns for the location app

from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    
    path("location/<token>/", send_location, name="send_location"),
    path("register/", register, name="register"),
    path("login/", login_view, name="login"),
    path('logout/', logoutaccount,name='logoutaccount'),
    path('user_track/', user_track, name='user_track'),
    path('token_summary/', token_summary, name='token_summary'),
]
