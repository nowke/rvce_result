from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api

from rvce import views
from rvce.api import resources

result_resource = resources.ResultResource()
subject_resource = resources.SubjectResource()

v1_api = Api(api_name='v1')
v1_api.register(result_resource)
v1_api.register(subject_resource)

urlpatterns = patterns('',
    url(r'^', include('rvce.urls', namespace='rvce')),
    url(r'^api/', include(v1_api.urls, namespace='resapi')),
    url(r'^admin/', include(admin.site.urls)),
)
