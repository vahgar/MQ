from django.shortcuts import render
from django.shortcuts import render,redirect
from .forms import LoginForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.http import HttpResponse, Http404
# Create your views here.
def base(request):
	return render(request,'base.html')

def login(request):
	form = LoginForm()
	context = {
	"form" : form,
	}
	return render(request,'account/login.html',context)

def signup(request):
	return render(request,'account/signup.html')
