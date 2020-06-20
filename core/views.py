from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser
from wallets.models import Wallet
from .services import assign_dedicated_account
# Create your views here.
@login_required(login_url="/signin")
def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':

        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            print(user)
            if user.wallet.bank is not None:
                auth_login(request, user)
                return redirect('/')
            else:
                auth_login(request, user)
                return redirect('/settings')
        else:
            print(form.errors)
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
                
                user.save()
                
                if user is not None:
                    auth_login(request, user)
                    return redirect('settings')
                else:
                    messages.info(request, 'Invalid details')
                    return redirect('signup')
    else:
        return render(request, 'signup.html')

@login_required(login_url='/signin')
def settings(request):
    user = request.user

    if request.method == 'POST':
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        middleName = request.POST['middleName']
        email = request.POST['email']
        address = request.POST['address']
        company = request.POST['company']
        state = request.POST['state']
        LGA = request.POST['LGA']
        BVN = request.POST['BVN']
         
        wallet_service = assign_dedicated_account(email, firstName, lastName, middleName, BVN, phone=user.phone)
        
        if wallet_service is not None:
            balance = wallet_service.get('amount', '0.00') 
            account_number = wallet_service.get('accountnumber', '')
            bank_name = wallet_service.get('bankname', '')
            account_name = wallet_service.get('accountName', '')
            account_status = wallet_service.get('accountstatus', '')
            flw_reference = wallet_service.get('flw_reference', '')

            wallet = Wallet.objects.create(
                    balance=balance,
                    transactionCounts=0,
                    accountNo=account_number,
                    bank= bank_name,
                    accountName= account_name,
                    BVN = BVN,
                    accountStatus = account_status,
                    accountReference = flw_reference
                )

            user.first_name = firstName
            user.last_name = lastName
            user.email = email
            user.address = address
            user.company = company
            user.state = state
            user.LGA = LGA
            user.wallet = wallet

            user.save()

            if user.wallet is not None:
                return redirect('/')
            else:
                messages.info(request, 'Invalid details')
            return redirect('settings')
    else:
        return render(request, 'settings.html')
    