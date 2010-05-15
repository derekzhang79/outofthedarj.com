from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response

def coming_soon(request):
    return render_to_response('coming_soon.html',)

def base_template(request):
    return render_to_response('base_template.html',)