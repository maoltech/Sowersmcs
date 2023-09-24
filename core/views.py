from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib import messages
from .models import User

# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        phone = request.POST['phone']
        password = request.POST['password']

        user = User.objects.get(phone=phone, password = password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid details')
            return redirect('login')

    return render(request, 'login.html')

def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        phone = request.POST['phone']
        password1 = request.POST['password1']
        print (username, password, phone, password1)
        if password != password1:
            messages.info(request, 'Password Does Not match')
            return redirect('signup')
        else:
            if User.objects.filter(phone=phone).exists():
                messages.info(request, 'Phone number already exist')
                return redirect('signup') 
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exist ')
                return redirect('signup') 
            else:
                user = User.objects.create(
                    username=username,
                    phone=phone,
                    password=password
                )
                user.save()
    else:
        return render(request, 'signup.html')