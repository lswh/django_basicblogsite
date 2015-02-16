from django.conf.urls import patterns, url

from blogsite import views

urlpatterns = patterns('',
    url(r'^$', views.homepage, name='homepage')
)