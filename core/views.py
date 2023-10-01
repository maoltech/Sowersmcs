from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser
from wallets.models import Wallet
# Create your views here.
@login_required(login_url="/signin")
def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':

        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid details')
            return redirect('/signin')

    return render(request, 'login.html')

@login_required(login_url="/signin")
def signout(request):
    auth_logout(request)
    return redirect('signin')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        phone = request.POST['phone']
        password1 = request.POST['password1']

        if password != password1:
            messages.info(request, 'Password Does Not match')
            return redirect('signup')
        else:
            if CustomUser.objects.filter(phone=phone).exists():
                messages.info(request, 'Phone number already exist')
                return redirect('signup') 
            elif CustomUser.objects.filter(username=username).exists():
                messages.info(request, 'Username already exist ')
                return redirect('signup') 
            else:                
                user = CustomUser.objects.create_user(
                    username=username,
                    phone=phone,
                    password=password
                )

                wallet = Wallet.objects.create(
                    balance=0.00,
                    transactionCounts=0,
                    accountNo=123456789,
                    bank="Bank",
                    accountName="account name"
                )
                user.wallet = wallet
                
                user.save()
                
                if user is not None:
                    return render(request, 'index.html', {"user": user} )
                else:
                    messages.info(request, 'Invalid details')
                    return redirect('signup')
    else:
        return render(request, 'signup.html')

# @login_required(login_url='/signin')
def settings(request):
    # user = CustomUser.objects.get(user=request.user)
    # print(user)
    return render(request, 'settings.html')