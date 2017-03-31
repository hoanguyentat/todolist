from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404, HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def login(request):
	return render(request, "admin/login.html")