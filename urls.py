from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin, auth
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^i18n/', include('django.conf.urls.i18n')),
    (r'^$', 'claims.views.index'),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
    (r'^accounts/profile/$', 'accounts.views.profile'),
    (r'^accounts/register/$', 'accounts.views.register'),
)

urlpatterns += patterns('claims.views',
    (r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', 'detail'),
    (r'^new/$', 'new'),
    (r'^(?P<id>\d+)/(?P<slug>[-\w]+)/edit/$', 'edit'),
    (r'^resolved/$', 'resolved'),
)