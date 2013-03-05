from django.conf.urls import patterns, include, url
from mysite import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls')),
    url(r'^tweeeter/', include('tweeeter.urls')),
    url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
    urlpatterns += patterns('', (r'^media/(?P<path>.*)$', 'django.views.static.serve', 
                                 {'document_root':'/home/rsnyder/helloWorld/mysite/mysite/media', 'show_indexes': True}), )