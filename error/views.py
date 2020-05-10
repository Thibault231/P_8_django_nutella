from django.shortcuts import render
from django.conf.urls import url
from . import views


def index(request):
    a= "hello world"
    return render(a)