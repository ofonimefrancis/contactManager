from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.add, name="addcontacts"),
    url(r'^list/$', views.list, name="listcontacts"),
]