# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from . import views
from .views import location, submit
urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('estimate/', location, name="location"),
    path('submit/', submit, name="submit"),


    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

    # path('location/', location, name="location"),

    # path('register/', register, name="register"),

]
