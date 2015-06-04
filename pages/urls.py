from django.conf.urls import patterns, include, url
from pages.views import *

urlpatterns = patterns('',
    # Examples:
	url(r'^$', home),
	url(r'^index', home),
	url(r'^contact', contact),
	url(r'^join', join),
	url(r'^about', about),
	url(r'^activities', activities),
	url(r'^ps', ps),
)
