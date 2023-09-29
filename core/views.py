from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User
from wallets.models import Wallet
from django.contrib.auth import login as auth_login, logout as auth_logout
# Create your views here.
@login_required(login_url="signin")
def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        phone = request.POST['phone']
        password = request.POST['password']

        user = User.objects.get(phone=phone, password=password)
        user_wallet = user.wallet

        if user is not None:
            return render(request, 'index.html', {"user": user, "wallet": user_wallet} )
        else:
            messages.info(request, 'Invalid details')
            return redirect('login')

    return render(request, 'login.html')

@login_required(login_url="signin")
def logOut(request):
    if request.method == 'POST':
        phone = request.POST['phone']
        password = request.POST['password']

        user = User.objects.get(phone=phone, password = password)

        if user is not None:
            auth_login(request, user)
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

                wallet = Wallet.objects.create(
                    balance=2000.00,
                    transactionCounts=0   
                )
                
                user = User.objects.create(
                    username=username,
                    phone=phone,
                    password=password,
                    wallet = wallet
                )
                
                user.save()
                
                if user is not None:
                    return render(request, 'index.html', {"user": user} )
                else:
                    messages.info(request, 'Invalid details')
                    return redirect('signup')
    else:
        return render(request, 'signup.html')
