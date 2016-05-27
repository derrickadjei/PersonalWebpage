from django.conf.urls import url
from . import views

app_name = 'aboutMe'

urlpatterns = [


    url(r'^$', views.index, name='index'),

    url(r'^resume/$', views.resume, name='resume'),


]