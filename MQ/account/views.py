from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
# Create your views here.
def base(request):
	return render(request,'base.html')

def login(request):
	return render(request,'account/login.html')

def signup(request):
	return render(request,'account/signup.html')
