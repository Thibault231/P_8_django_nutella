from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^result/$', views.result, name='result'),
    url(r'^item/(?P<item_id>[0-9]+)/$', views.item, name='item'),
    url(r'^history/$', views.history, name='history'),
    url(r'^connexion/$', views.connexion, name='connexion'),
    url(r'^deconnexion/$', views.deconnexion, name='deconnexion'),
    url(r'^count_creation/$', views.count_creation, name='count_creation'),
    url(r'^save/(?P<item_id>[0-9]+)/$', views.save, name='save'),
]