# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import Point, Location, Estimate, Property, Rebate, Eligibility, Consumption


# Register your models here.
admin.site.register(Point)
admin.site.register(Location)
admin.site.register(Estimate)
admin.site.register(Property)
admin.site.register(Rebate)
admin.site.register(Eligibility)
admin.site.register(Consumption)
