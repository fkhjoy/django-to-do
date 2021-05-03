from django.contrib import auth
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError

# Create your views here.

def home(request):
    return render(request, 'todo/home.html')

def signupuser(request):

    if request.method == 'GET':
        return render(request, 'todo/signupuser.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenttodos')

            except IntegrityError:
                return render(request, 'todo/signupuser.html', {'form': UserCreationForm, 'error':"User already exists"}, status=400)
        else:
            return render(request, 'todo/signupuser.html', {'form': UserCreationForm, 'error':"Passwords didn't match"}, status=400)
        
        # return HttpResponse("Done")

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'todo/loginuser.html', {'form': AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if not user:
            return render(request, 'todo/loginuser.html', {'form': AuthenticationForm, 'error':"Username and Password didn't match"}, status=400)
        else:
            login(request, user)
            return redirect('currenttodos')

def logoutuser(request):
    # pass
    if request.method == "POST":
        logout(request)
        return redirect('home')

def currenttodos(request):
    return render(request, 'todo/currenttodos.html')