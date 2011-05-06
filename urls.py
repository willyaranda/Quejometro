from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^i18n/', include('django.conf.urls.i18n')),
    (r'^$', 'claims.views.index'),
)

urlpatterns += patterns('claims.views',
    (r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', 'detail'),
    (r'^new/$', 'new'),
    (r'^(?P<id>\d+)/(?P<slug>[-\w]+)/edit/$', 'edit'),
    (r'^resolved/$', 'resolved'),
)

#urlpatterns += patterns('users.views',
#    (r'')