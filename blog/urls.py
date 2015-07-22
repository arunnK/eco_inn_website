from django.conf.urls import patterns, include, url
from blog.views import *

urlpatterns = patterns('',
    # Examples:
	url(r'^blog', blog),
	url(r'^post1', post1),
	url(r'^post2', post2),
	url(r'^post3', post3),
	url(r'^post4', post4),
	url(r'^post5', post5),
	url(r'^post6', post6),
	url(r'^post7', post7),
)
