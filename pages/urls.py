from django.urls import path
from .views import hello, v

urlpatterns=[
	path("", hello,name="home"),
        path("v/", v),
]
