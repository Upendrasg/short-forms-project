# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# from .forms import PointForm
from .models import Estimate, Point, Location
from .forms import EstimateForm, LocationForm, PointForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.template import loader
from django.http import HttpResponse
from django import template

@login_required(login_url="/login/")
def index(request):
    
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))


def location(request):
    if request.method == "POST":
        
        point_form = PointForm(request.POST)
        location = LocationForm(request.POST)
        estimate = EstimateForm(request.POST)
        if point_form.is_valid() and location.is_valid() and estimate.is_valid(): # All validation rules pass
                print( "all validation passed")
                primary = point_form.save()
                location.cleaned_data["point"] = primary
                location_obj = location.save()
                estimate.cleaned_data["location"] = location_obj
                estimate.save()
        else:
            msg = 'Form in not valid' 
        
    context = {}
    context['segment'] = 'point.html'
    html_template = loader.get_template('point.html')
    return HttpResponse(html_template.render(context, request))


def submit(request):
    if request.method == "GET":
        context = {}
        context['segment'] = 'property.html'
        # form = PointForm()
        form = EstimateForm()
        html_template = loader.get_template('property.html')
        # return HttpResponse(html_template.render(context, request))
        return render(request, "property.html", {"form": form})

# def submit(request):
#     # form = PointForm()
#     if request.method == 'POST' and request.FILES:
#         primary_form = PointForm(request.POST, prefix = "primary")
#         b_form = LocationForm(request.POST, prefix = "b")
#         c_form = EstimateForm(request.POST, prefix = "c")
#         if primary_form.is_valid() and b_form.is_valid() and c_form.is_valid(): # All validation rules pass
#                 print( "all validation passed")
#                 primary = primary_form.save()
#                 b_form.cleaned_data["primary"] = primary
#                 b = b_form.save()
#                 c_form.cleaned_data["primary"] = primary
#                 c = c_form.save()
#                 return render ("/point.html")
#         else:
#                 print ("failed")

#     else:
#         primary_form = PointForm(prefix = "primary")
#         b_form = LocationForm(prefix = "b")
#         c_form = EstimateForm(prefix = "c")
#     return render(request, 'point.html', {
#     'primary_form': primary_form,
#     'b_form': b_form,
#     'c_form': c_form,
#     })

    # BookFormSet = inlineformset_factory(Location, Estimate, form=EstimateForm)
    # print("BookFormSet========", BookFormSet)
    # if request.method == 'POST':
    #     formset = BookFormSet(request.POST)
    #     print("formset==========", formset)
    #     if formset.is_valid():
    #         formset.save()
    # else:
    #     formset = BookFormSet()
    # print("formset==========", formset)
    # return render_to_response("point.html", {"formset": formset})
    