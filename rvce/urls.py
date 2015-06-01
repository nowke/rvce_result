from django.conf.urls import patterns, url

from rvce import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^search/', views.search, name='search'),
    url(r'^xyzzy/', views.populate, name='populateResult'),
    url(r'^stats/$', views.stats, name='stats'),
    url(r'^stats/sub/(?P<dept>[a-z]{2,3})/(?P<sem>[1-8]{1})/$', views.stats_sub, name='stats_sub'),
    url(r'^stats/dept/(?P<sem>([1-8]{1})|(All))/$', views.stats_dept, name='stats_dept'),
)