from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^result/$', views.result, name='result'),
    url(r'^item/(?P<item_id>[0-9]+)/$', views.item, name='item'),
    url(r'^history/$', views.history, name='history'),
    url(r'^save/(?P<item_id>[0-9]+)/$', views.save, name='save'),
    url(r'^legal/$', views.legal, name='legal'),
    url(r'^pindex/$', views.pindex, name='pindex'),
]