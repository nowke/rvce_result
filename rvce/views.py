from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UploadJSONForm
from .models import Result, Subject
from .stat import StatSub, StatDept
from .helpers import handle_json_file, add_result, get_result_usn, get_sub_name, get_result_name, get_result_name_branch, dept_map
import ast
import difflib

def index(request):

	front_page = True
	usn_entered = ''

	if request.method == 'GET':
		stud_dict = None

	elif request.method == 'POST':
		usn_entered = request.POST.get("stud_usn", "")
		USN = '1RV%s' % (usn_entered.upper())
		stud_dict = Result.objects.filter(result_usn=USN)
		if stud_dict:
			stud_dict = stud_dict[0]
			sub_list = []
			sub_dict_a = stud_dict.result_sub

			for subcode in sub_dict_a:
				sub_objs = Subject.objects.filter(sub_code=subcode)[:1]
				sub_name = sub_objs[0].sub_name
				sub_dict = {
					"sub_code": subcode,
					"sub_title": sub_name,
					"sub_grade": sub_dict_a[subcode]
				}
				sub_list.append(sub_dict)

			stud_dict.result_sub = sub_list

		front_page = False

	context = {
		'stud_details': stud_dict,
		'entered_usn': usn_entered,
		'front_page': front_page
	}

	return render(request, 'rvce/main.html', context)

def search(request):

	selected = ['' for x in range(12)]
	if request.method == 'GET':
		selected[0] = ' selected'
		context = {
			'search_results': None,
			'search_query': '',
			'selected': selected,
		}

	elif request.method == 'POST':
		name = query = request.POST.get("searchName", "")
		option = request.POST.get("stud_dept", '')
		name_split = name.split(" ")
		result_objects = []

		if option == 'All':
			for word in name_split:
				result_objects = Result.objects.filter(result_name__icontains=word)
			selected[0] = ' selected'
		else:
			dept = dept_map(option)[0]
			for word in name_split:
				result_objects = Result.objects.filter(result_name__icontains=word, result_branch=dept)
			selected[dept_map(option)[1]] = ' selected'

		result_objects = list(set(result_objects))
		result_objects = sorted(result_objects, 
								key=lambda x: difflib.SequenceMatcher(None, x.result_name, name.upper()).ratio(),
								reverse=True)

		print result_objects
		context = {
            'search_results': result_objects[:20],
            'selected': selected,
            'search_query': query,
        }

	return render(request, 'rvce/search.html', context)

def populate(request):
	if request.method == 'GET':
		return render(request, 'rvce/populate.html')
	elif request.method == 'POST':
		form = UploadJSONForm(request.POST, request.FILES)
		stud_list = handle_json_file(request.FILES['file'])

		add_result(stud_list)

		return HttpResponse("\nFile uploaded")

def stats(request):
	departments = dept_map(0, only_keys=True)

	context = {
		'depts': departments,
	}
	return render( request, 'rvce/stats.html', context)

def stats_sub(request, dept, sem):
	dept_full = dept_map(dept, three=True)
	sem = int(sem)

	sub_stat_dict = StatSub(dept_full, sem)
	context = {
		'sub_stat_dict': sub_stat_dict
	}
	return render(request, 'rvce/stats-sub.html', context)

def stats_dept(request, sem):

	dept_dict = StatDept(sem)
	
	context = {
		'dept_dict': dept_dict,
		'sem': sem
	}

	return render(request, 'rvce/stats-dept.html', context)
