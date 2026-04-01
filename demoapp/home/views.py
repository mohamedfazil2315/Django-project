from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, 'home/index.html')

def login_view(request):
    if request.method == "POST":
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('/')
    return render(request, 'home/login.html')

def signup_view(request):
    if request.method == "POST":
        User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password']
        )
        return redirect('/login/')
    return render(request, 'home/signup.html')
