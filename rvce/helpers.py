import simplejson as json
import requests
from django.core.urlresolvers import reverse

from .models import Result, Subject

urlres = 'http://0.0.0.0:5000/api/v1/result/'
urlsub = 'http://0.0.0.0:5000/api/v1/subject/'

headers = {
	'Content-Type' : 'application/json',
	'Authorization': 'Apikey nowke:0088d77547a69cdcbf3eebdf32254f65a02689a7'
}

def handle_json_file(f):
	with open('up.json', 'wb+') as dest:
		for chunk in f.chunks():
			dest.write(chunk)

	with open('up.json', 'r') as jfile:
		content = json.load(jfile)
		return content

def add_result(stud_list):
	# url = reverse('resapi', args='', kwargs={'resource_name': 'result', 'api_name': 'v1'})

	# sub_dict = {}
	# for subject in stud_dict['subjects']:
	# 	sub_dict[subject['sub_code']] = subject['sub_grade']
	
	# payload = {
	# 	"result_name": stud_dict['name'],
	# 	"result_usn": stud_dict['usn'],
	# 	"result_sem": int(stud_dict['sem']),
	# 	"result_sgpa": float(stud_dict['sgpa']),
	# 	"result_branch": stud_dict['branch'],
	# 	"result_sub": sub_dict
	# }

	# r = requests.post(urlres, data=json.dumps(payload), headers=headers)

	# """
	# Subject Field
	# """

	# for subject in stud_dict['subjects']:
	# 	mpayload = {
	# 		"sub_code": subject['sub_code'],
	# 		"sub_name": subject['sub_title']
	# 	}
	# 	requests.post(urlsub, data=json.dumps(mpayload), headers=headers)
	split_dict = split_into(stud_list, 25)
	for student_list in split_dict:
		bulk_obj = []
		for student in student_list:
			sub_dict = {}
			for subject in student['subjects']:
				sub_dict[subject['sub_code']] = subject['sub_grade']

			student_obj = Result(
				result_name= student['name'],
				result_usn = student['usn'],
				result_sem = int(student['sem']),
				result_sgpa = float(student['sgpa']),
				result_branch = student['branch'],
				result_sub = sub_dict,
			)
			bulk_obj.append(student_obj)
			# Subject

			for subject in student['subjects']:
				sobjs = Subject.objects.filter(
					sub_name=subject['sub_title'],
					sub_code=subject['sub_code'],
					sub_sem= int(student['sem']),
					sub_branch = student['branch']
				)
				if not sobjs:
					s = Subject(
						sub_code = subject['sub_code'],
						sub_name = subject['sub_title'],
						sub_sem = int(student['sem']),
						sub_branch = student['branch'],
					)
					s.save()


		Result.objects.bulk_create(bulk_obj)

def get_result_usn(usn):
	payload = {
		"result_usn": usn,
	}	
	r = requests.get(urlres, params=payload, headers=headers)
	if r.json()['meta']['total_count'] == 1:
		return r.json()['objects'][0]
	return None

def get_sub_name(subcode):
	payload = {
		"sub_code": subcode,
	}
	r = requests.get(urlsub, params=payload, headers=headers)
	return r.json()['objects'][0]['sub_name']

def get_result_name(name):
	payload = {
		"result_name__icontains": name,
	}
	r = requests.get(urlres, params=payload, headers=headers)
	if r.json()['meta']['total_count'] >= 1:
		return r.json()['objects']
	return []

def get_result_name_branch(name, dept):
	payload = {
		"result_name__icontains": name,
		"result_branch": dept,
	}
	r = requests.get(urlres, params=payload, headers=headers)
	if r.json()['meta']['total_count'] >= 1:
		return r.json()['objects']
	return []	

def split_into(lst, n):
    new_list = []
    new_list.append([])
    c = 0
    for i in range(len(lst)):
        if (i + 1) % n == 0:
            new_list.append([lst[i]])
            c += 1
        else:
            new_list[c].append(lst[i])
    return new_list

def dept_map(index, only_keys=False, three=False, lst=False, rev=False):
	dmap = {
		'Biotech': ['Bio Technology',1],
		'Chemical': ['Chemical Engineering', 2],
		'Civil': ['Civil Engineering', 3],
		'CSE': ['Computer Science Engineering', 4],
		'EEE': ['Electrical and Electronics Engg.', 5],
		'ECE': ['Electronics and Communication Engg.', 6],
		'IEM': ['Industrial Engg & Management', 7],
		'ISE': ['Information Science', 8],
		'IT': ['Instrumentation Technology', 9],
		'Mechanical': ['Mechanical Engineering', 10], 
		'Telecom': ['Telecommunication Engineering', 11],
	}
	if only_keys: 
		return dmap.keys()
	elif three:
		map2 = dict(zip([x.lower()[:3] for x in dmap.keys()], [x[0] for x in dmap.values()]))
		return map2.get(index, None)
	elif lst:
		return [x[0] for x in dmap.values()]
	elif rev:
		map2 = dict(zip([x[0] for x in dmap.values()], [x for x in dmap.keys()]))
		return map2.get(index, None)
	return dmap.get(index, None)