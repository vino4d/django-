from django.urls import path
from .views import *

urlpatterns=[
	path("", hello, name="home"),
        path("v/", v, name="v"),
        path("home/",HomePageView.as_view(), name='hp'),
        path("about/",aboutPageView.as_view(), name='ap'),
]
