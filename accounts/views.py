from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http.request import HttpRequest
# Create your views here.

def home(req):
    return redirect('login')

def login(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        user = auth.authenticate(request=req,username = username ,password = password)
        if user is not None:
            auth.login(req , user)
            messages.success( req, 'You have successfully logged in')
            return redirect('inside')
        else:
            messages.error(req, 'Username or Password is incorrect')
            return redirect('login')
        
    else:
        return render(req, 'accounts/login.html')

def signup(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        password2 = req.POST['password2']

        if password == password2:
            
            if User.objects.filter(username=username).exists():
                messages.error(req, 'Try another username')
                return redirect(signup) 
            else:
                user = User.objects.create_user(username = username, password=password)
                user.save()
                messages.success(req, 'You are registered and can log in')
                return redirect('login')
        else:
            messages.error(req, 'Passwords do not match!')
            return redirect('signup')
    else:
        return render(req, 'accounts/signup.html')


def logout(req):
    if req.method == 'POST':
        auth.logout(req)
        messages.success(req, 'You have logged out')
    return redirect('login')

def inside(req):
    if req.user.is_authenticated:
        return render(req, 'accounts/inside.html')
    else:
        messages.error(req, 'You must login first.')
        return redirect('login')


