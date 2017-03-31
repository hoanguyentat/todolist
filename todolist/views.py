from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404, HttpRequest, HttpResponse, HttpResponseRedirect
from .models import Task
from django.urls import reverse
from datetime import datetime
# Create your views here.

def index(request):
	tasks_list = Task.objects.order_by("-pub_date")
	return render(request, "todolist/index.html", {'tasks_list' : tasks_list})
		
def add_task(request):
	# print request.read()
	task_content = request.POST['context']
	date = request.POST['deadline']
	now = datetime.now()
	time_task = "%s-%s-%s %s:%s" % (now.year, now.month, now.day, now.hour, now.minute)
	task = Task(context = task_content, pub_date=time_task, status=0, deadline = date)
	task.save()
	return redirect('/todolist')
def done_task(request):
	data = request.POST
	for x in data:
		if x == "csrfmiddlewaretoken":
			pass
		else:
			task = get_object_or_404(Task,pk=data[x])
			task.status = 1
			task.save()
	return redirect('/todolist')