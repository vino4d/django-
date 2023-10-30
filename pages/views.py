from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hello(request):
    return HttpResponse('<h1> "jj" <h1/>')

def v(request):
    return HttpResponse("vvvvvvvv")
