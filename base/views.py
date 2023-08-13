from django.shortcuts import render, redirect
from account.models import Referral, Transactions
from authentication.forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.db.models import Sum

# Create your views here.


def Login(request):
    login_form = LoginForm()
    if request.method == "POST":
        login_form = LoginForm(data=request.POST)
        if login_form.is_valid():
            email = request.POST["email"]
            password = request.POST["password"]
            user = authenticate(username=email, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return redirect('base:home')
                else:
                    print("User is not activated yet")
            else:
                print("User is none")
    context = {
        'form': login_form
    }
    return render(request,"login.html", context)


def logout_view(request):
    logout(request)
    return redirect("/")


def home(request):

    context = {
        
        }
    return render(request,"dashboard.html", context)

def withdraw(request):
    context = {
        # "approved_withdrawals": approved_withdrawals,
        # "pending_withdrawals": pending_withdrawals,
        # "refferals_earnings": refferals_earnings,
        
        }
    return render(request,"withdraw.html", context)

def profile(request):
    context = {
        # "approved_withdrawals": approved_withdrawals,
        # "pending_withdrawals": pending_withdrawals,
        # "refferals_earnings": refferals_earnings,
        
        }
    return render(request,"profile.html", context)

def how(request):
    context = {
        # "approved_withdrawals": approved_withdrawals,
        # "pending_withdrawals": pending_withdrawals,
        # "refferals_earnings": refferals_earnings,
        
        }
    return render(request,"how-to.html", context)

def tasks(request):
    context = {
        # "approved_withdrawals": approved_withdrawals,
        # "pending_withdrawals": pending_withdrawals,
        # "refferals_earnings": refferals_earnings,
        
        }
    return render(request,"tasks.html", context)

def referrals(request):
    referrals_count = Referral.objects.filter(referrer=request.user.profile).count()
    context = {
        "referrals_count": referrals_count,
        # "pending_withdrawals": pending_withdrawals,
        # "refferals_earnings": refferals_earnings,
        
        }
    return render(request,"referral.html", context)
