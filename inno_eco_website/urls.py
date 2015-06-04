from django.conf.urls import patterns, include, url
from django.contrib import admin 
#from django import  blog

urlpatterns = patterns('',
    # Examples:
    url(r'', include('blog.urls')),
    url(r'', include('pages.urls')),
    

    url(r'^admin/', include(admin.site.urls)),
)
