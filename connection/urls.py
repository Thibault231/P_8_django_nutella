# coding: utf-8
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^connexion/$', views.connexion, name='connexion'),
    url(r'^myaccount/$', views.myaccount, name='myaccount'),
    url(r'^deconnexion/$', views.deconnexion, name='deconnexion'),
    url(r'^count_creation/$', views.count_creation, name='count_creation'),
]
