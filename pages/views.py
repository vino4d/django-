from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Post

def hello(request):
    return HttpResponse("iii")

def v(request):
    return HttpResponse("vvvvvvvv")

#to create template view needs class
class HomePageView(TemplateView):
    model= Post
    template_name= "home1.html"
class aboutPageView(TemplateView):
    template_name= "about1.html"
