from django.shortcuts import render, redirect
from account.models import Referral, Transactions, UserProfile
from authentication.forms import LoginForm, NewUserForm
from django.contrib.auth import authenticate, login, logout
from django.db.models import Sum
from django.contrib.auth import get_user_model


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

def signup(request):
    refe = request.GET.get("ref")
    form = NewUserForm(initial={"referral_code": refe})

    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            reffered = UserProfile.objects.get(user=user)
            try:
                ref_user = get_user_model().objects.get(username=refe)
                try:
                    refferal = UserProfile.objects.get(user=ref_user)
                    Referral.objects.create(referrer=refferal, referred_user=reffered)
                    refferal.account_balance += 100
                    refferal.save()
                    Transactions.objects.create(user=get_user_model().objects.get(username=refe), type="R", amount=100, balance=refferal.account_balance)
                except UserProfile.DoesNotExist:
                    print("2")
            except get_user_model().DoesNotExist:
                print("None")
            
            login(request, user)
            return redirect("base:home")
            
            # messages.success(request, "Registration successful." )
        # messages.error(request, "Unsuccessful registration. Invalid information.")
    context = {
        'form': form
    }
    return render(request,"register.html", context)



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