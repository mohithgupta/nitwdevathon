from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from .models import *
# Create your views here.
#curruser = ''

def login(request):
    if request.method=="POST":
        print(request.POST.keys())
        name = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm = request.POST['Confirm']
        usertype = bool(request.POST['usertype']=='Teacher')
        if password==confirm:
            if User.objects.filter(username=name).exists():
                messages.info(request, 'Username taken')
                return redirect('/')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
                return redirect('/')
            else:
                user = User.objects.create_user(username = name,email = email, password = password, is_staff = usertype)
                user.save()
                #return render(request, 'signin')
                return redirect('signin')

        else:
            messages.info(request, 'Please enter the same password')
        #return render(request, 'home.html')
        return redirect('/')

    else:
        return render(request, 'signup.html')
    #if request.method =='GET':
def signin(request):
    if request.method=='POST':
        name = request.POST['username']
        password = request.POST['password']
        #curruser = name
        print(1)
        user = auth.authenticate(username=name, password=password)
        if user is not None:
            auth.login(request, user)
            #return HttpResponse("Hi")
            return redirect('select')
        else:
            messages.info(request, 'invalid credentials')
        return redirect('signin')
    else:
        return render(request, 'login-page.html')

def select(request):
    print(1)
    return HttpResponse('Hi')
