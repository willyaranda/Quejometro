# coding=utf-8
from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^i18n/', include('django.conf.urls.i18n')),
    (r'^$', 'quejas.views.index'),
)

urlpatterns += patterns('quejas.views',
    #(r'^usuario/(?P<slug>[-\w]+)$', 'usuario.views.nuevo'),
    #(r'^nuevo/$', 'quejas.views.nuevo'),
    #Le pasamos a quejas/view.py función detalle el parámetro request y slug
    (r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', 'detalle'),
    (r'^nueva/$', 'nueva'),
)