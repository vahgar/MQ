from django.shortcuts import render
from django.shortcuts import render,redirect
from .forms import LoginForm,SignUp
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.http import HttpResponse, Http404
# Create your views here.


def base(request):
	return render(request,'base.html')


@require_GET
def login(request):
	if request.user.is_authenticated():
		print('Already Looged In')
		return render(request,'home.html')
	else:
		form = LoginForm()
		context = {
		"form" : form,
		}
	return render(request,'account/login.html',context)

def signup(request):
	form = SignUp(request.POST)
	if form.is_valid():
		user=form.save();
		f=LoginForm()
		return render(request,'account/login.html',{'f':form})
	else:
		context = {"form":form}
		return render(request,'account/signup.html',context)

@require_POST
def handle_login(request):

	if request.user.is_authenticated():
		print("Logged In")
		return render(request,'home.html')
	f = LoginForm(request.POST)
	if f.is_valid():
		user = f.get_user();
		auth_login(request,user)
		print('asxiuahha')
		return render(request,'home.html')
	if not f.is_valid():
		print("X")
		form = LoginForm()
		Error = "*Invalid Username or Password"
		context = {'form':form,'Error':Error}
		return render(request,'account/login.html',context)

@require_GET
def logout(request):
	auth_logout(request)
	return render(request,'base.html')


