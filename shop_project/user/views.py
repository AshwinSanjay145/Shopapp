from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Exist")
                return redirect('user:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email taken already")
                return redirect('user:register')
            else:
                user=User.objects.create_user(first_name=firstname,last_name=lastname,username=username,email=email,password=password)
                user.save()
                messages.info(request,"Account Created")
                print("create user")
        else:
            messages.info(request,"Password mismatched")
            print("password mismatched")
            return redirect('user:register')
    return render(request,"register.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Check username and password")
            return redirect('user:login')

    return render(request,"login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')
