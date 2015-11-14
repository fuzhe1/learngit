"""fuzhe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from app0.views import Information,home,Add,Search,Change,AddAuthor
from django.template import RequestContext
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zhe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^home/$',home),
	url(r'^Add/$',Add),
	url(r'^Search/$',Search),
	url(r'^Information/(.+)/$',Information),
	url(r'^Change/(.+)/$',Change),
	url(r'^AddAuthor/$',AddAuthor),
)


















