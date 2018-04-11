from django.conf.urls import include, url
from . import views



urlpatterns = [
    url(r'^track/$',views.index,name='index'),
    url(r'^track/new/$',views.new_culture,name='new'),
    url(r'^track/test/(?P<id>[0-9]+)/$',views.testc,name='testc'),
    url(r'^track/imagetest/(?P<id>[0-9]+)/$',views.imagetest,name='imagetest'),
    url(r'^track/result/(?P<id>[0-9]+)/$',views.result,name='result'),
    url(r'^track/delete/(?P<id>[0-9]+)/$',views.delete_culture,name='delete'),

]
