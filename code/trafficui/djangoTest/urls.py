from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
urlpatterns = patterns('',
    # Examples:
    #prefix, *args url(r'^$', 'djangoTest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^site_media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_PATH}),
    url(r'^infor/', include('backtest.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^add/', include('backtest.urls')),
    url(r'^traffic/', include('traffic.urls')),
)
