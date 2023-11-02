from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import TemplateView

def hello(request):
    return HttpResponse("iii")

def v(request):
    return HttpResponse("vvvvvvvv")

class HomePageView(TemplateView):
    template_name= "home1.html"
class aboutPageView(TemplateView):
    template_name= "about1.html"
