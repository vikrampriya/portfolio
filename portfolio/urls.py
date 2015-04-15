from django.conf.urls import patterns, include, url
from django.contrib import admin

# Url Patterns from the root. 
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^aboutme/', 'blog.views.aboutme'),
    url(r'^contact/', 'blog.views.contact'),
    url(r'^$', 'blog.views.index'),
    url(r'^(?P<slug>[\w\-]+)/$', 'blog.views.post'),
)
