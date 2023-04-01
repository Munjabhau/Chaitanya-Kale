from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *


def home(request):
    return render(request, 'home/home.html')


def about(request):
    return render(request, 'home/about.html')


def contact(request):
    if request.method == "POST":
        fullName = request.POST.get('fullName')
        email = request.POST.get('email')
        msg = request.POST.get('msg')
        try:
            if (len(fullName) < 2 or len(email) < 4 or len(msg < 4)):
                messages.error(request, "Please fill all the details ")
            else:
                saveContact = ContactModel(fullName=fullName, email=email, msg=msg)
                saveContact.save()
                messages.success(request, "Your message send successfully")
        except Exception as e:
            print(e)
    return render(request, 'home/contact.html')


def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        fname = request.POST['fname']
        lname = request.POST['lname']
        password = request.POST.get('password')
        try:
            if User.objects.filter(username=username).first():
                messages.error(request, "username is already taken")
                return redirect('/register')
            if User.objects.filter(email=email).first():
                messages.error(request, "EmailId is already taken")
                return redirect('/register')
            if len(username) < 2 or len(email) < 2 or len(fname) < 2 or len(lname) < 2 or len(password) < 2:
                messages.error(request, 'Please fill the details correctly')
                return redirect('/register')
            else:
                user_obj = User(username=username, email=email)
                user_obj.set_password(password)
                user_obj.first_name = fname
                user_obj.last_name = lname
                user_obj.save()
        except Exception as e:
            print(e)
    return render(request, 'home/register.html')


def login_attempt(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username=username).first()
        if user_obj is None:
            messages.success(request, "User not found with this username")
            return redirect('/login')
        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, 'Please enter correct password')
            return redirect('/login')
        login(request, user)
        return redirect('/')
    return render(request, 'home/login.html')


def user_logout(request):
    logout(request)
    messages.success(request, 'Logout Successfully')
    return redirect('/login')


def project(request):
    allProject = ProjectModel.objects.all()
    context = {'allProject': allProject}
    return render(request, 'home/project.html', context)
