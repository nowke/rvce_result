from tastypie.resources import ModelResource, ALL
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import Authorization
from rvce.models import Result, Subject

class ResultResource(ModelResource):
	class Meta:
		queryset = Result.objects.all()
		resource_name = "result"
		filtering  = {
			"result_usn": ALL,
			"result_name": ['icontains'],
			"result_branch": ALL
		}
		allowed_methods = ['get', 'post']
		authentication = ApiKeyAuthentication()
		authorization = Authorization()
		# curl http://localhost:5000/api/v1/result/?result_usn=1RV13CS090

class SubjectResource(ModelResource):
	class Meta:
		queryset = Subject.objects.all()
		result_name = "subject"
		filtering = {
			"sub_code": ALL
		}
		allowed_methods = ['get', 'post']
		authentication = ApiKeyAuthentication()
		authorization = Authorization()