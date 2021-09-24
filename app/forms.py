from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from .models import Point, Estimate, Location

# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    """
    """
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",                
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",                
                "class": "form-control"
            }
        ))


class PointForm(forms.ModelForm):
    class Meta:
        model = Point
        fields = "__all__"  


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        exclude = ('point',)


class EstimateForm(forms.ModelForm):
    class Meta:
        model = Estimate
        fields = "__all__"  
        exclude = ('location',)

