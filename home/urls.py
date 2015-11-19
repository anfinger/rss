from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.aktuelles, name='aktuelles'),
    url(r'^aktuell/(?P<pk>[0-9]+)/$', views.aktuell_detail, name='aktuell_detail'),
    url(r'^new/$', views.aktuell_neu, name='aktuell_neu'),
    url(r'^aktuell/(?P<pk>[0-9]+)/edit/$', views.aktuell_edit, name='aktuell_edit'),
]
