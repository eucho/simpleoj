# Create your views here.
from django.http import HttpResponse
from problems.models import Problem, Submission
from django.shortcuts import render
from django.http import Http404
from django.utils import timezone

def index(request):
	problems = Problem.objects.all()
	context = {'problems': problems}
	return render(request, 'problems/index.html', context)

def submit(request, problem_id):
	try:
		p = Problem.objects.get(pk=problem_id)
	except Problem.DoesNotExist:
		return HttpResponse('Problem not found')
	else:
		context = {'problem_id': problem_id,
					'title': p.title,}
		return render(request, 'problems/submit.html', context)

def judge(request):
	try:
		s = Submission(
				submit_time=timezone.now(),
				source=request.POST['source'],
				result=request.POST['result'])
		p = Problem.objects.get(pk=int(request.POST['pid']))
		p.submission_set.add(s)
	except:
		return HttpResponse('POST Error!')
	else:
		return HttpResponse('POST Success!')

def showproblem(request, problem_id):
	try:
		p = Problem.objects.get(pk=problem_id)
		sub_times = p.submission_set.count()
		ac_times = [x for x in p.submission_set.all() if x.result == 'Yes']
	except Problem.DoesNotExist:
		raise Http404
	else:
		context = {'problem': p, 
			'sub_times': sub_times, 
			'ac_times':len(ac_times)}
		print 'sub_times', sub_times
		return render(request, 'problems/showproblem.html', context)
