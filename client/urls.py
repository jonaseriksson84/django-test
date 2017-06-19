from django.conf.urls import url
from client import views


urlpatterns = [
    url(r'^client/(?P<path>.*)/$', views.index),
    url(r'^client/$', views.index),
]
