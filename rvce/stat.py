from .models import Result, Subject
from .helpers import dept_map
from pprint import pprint

def StatSub(dept, sem):
	sub_objs = Subject.objects.filter(sub_branch=dept, sub_sem=sem)
	sub_dict_stat = {}
	for sub in sub_objs:
		subcode = sub.sub_code
		stud_objs = Result.objects.filter(result_branch=dept, result_sem=sem, result_sub__contains=subcode)
		sub_dict_stat[subcode] = {'title': sub.sub_name, 'stat':{}}
		for stud in stud_objs:
			grade = stud.result_sub[subcode]
			if grade in sub_dict_stat[subcode]['stat']:
				sub_dict_stat[subcode]['stat'][grade] += 1
			else:
				sub_dict_stat[subcode]['stat'][grade] = 1

	return sub_dict_stat

def StatDept(sem='All'):
	dept_dict = {}

	for dept in dept_map(0, lst=True):
		if sem == 'All':
			stud_objs = Result.objects.filter(result_branch=dept)
		else:
			stud_objs = Result.objects.filter(result_branch=dept, result_sem=int(sem))
		if not stud_objs: break
		sgpa_sum = 0.0
		for stud in stud_objs:
			sgpa_sum += stud.result_sgpa
		avg_sgpa = sgpa_sum / len(stud_objs)
		dept_short = dept_map(dept, rev=True)
		dept_dict[dept_short] = round(avg_sgpa, 2)
	
	return dept_dict		
