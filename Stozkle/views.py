from django.shortcuts import render
from myStock.models import Member, Equipment
from django.contrib.auth.models import User
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout as auth_logout, login as auth_login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

def home(request):
	main = "Hi There!"
	if request.user.is_authenticated():
		user = request.user
		member = Member.objects.get(user = user)
		main = 'Welcome Back! ' + member.nick_name
	else:
		user = ''
		member = ''
	return render(request, 'home.html', {'main': main, 'user': user, 'member': member})

def login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse('Your account is disabled.<br><a href="/">Back to Home Page?</a>')
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse('Invalid login details supplied.<br><a href="/">Back to Home Page?</a>' )
    else:
        return render_to_response('login.html', {}, context)

@login_required(login_url='/login/')
def logout(request):
	auth_logout(request)
	return render(request, 'home.html', {'main': 'Hi There!'})