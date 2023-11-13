from django.shortcuts import render, redirect
from account.models import Coupon, Referral, Transactions, UserProfile
from authentication.forms import CouponForm, LoginForm, NewUserForm, WithdrawalForm
from django.contrib.auth import authenticate, login, logout
from django.db.models import Sum
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages



# Create your views here.

def index(request):
    context = {}
    return render(request,"home.html", context)
def Login(request):
    if request.user.is_authenticated:
        return redirect("base:home")
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
                    messages.success(request, "Login successful", extra_tags="alert-success")
                    return redirect('base:home')
                else:
                    messages.error(request, "Your account is not activated", extra_tags="alert-danger")
            else:
                messages.error(request, "Invalid email/password", extra_tags="alert-danger")
    context = {
        'form': login_form
    }
    return render(request,"login.html", context)


def first_login(request):
    if request.user.is_authenticated:
        return redirect("base:home")
    login_form = LoginForm()
    if request.method == "POST":
        login_form = LoginForm(data=request.POST)
        if login_form.is_valid():
            email = request.POST["email"]
            password = request.POST["password"]
            user = authenticate(username=email, password=password)
            if user:
                if user.is_active:
                    if user.first_app:
                        login(request, user)
                        messages.success(request, "Login successful", extra_tags="alert-success")
                        return redirect('base:home')
                    else:
                        user_profile = UserProfile.objects.get(user=user)
                        user_profile.account_balance += 500
                        user.first_app = True
                        user.save()
                        user_profile.save()
                        login(request, user)
                        messages.success(request, "Login successful", extra_tags="alert-success")
                        return redirect('base:home')
                else:
                    messages.error(request, "Your account is not activated", extra_tags="alert-danger")
            else:
                messages.error(request, "Invalid email/password", extra_tags="alert-danger")
    context = {
        'form': login_form
    }
    return render(request,"login.html", context)

def second_login(request):
    if request.user.is_authenticated:
        return redirect("base:home")
    login_form = LoginForm()
    if request.method == "POST":
        login_form = LoginForm(data=request.POST)
        if login_form.is_valid():
            email = request.POST["email"]
            password = request.POST["password"]
            user = authenticate(username=email, password=password)
            if user:
                if user.is_active:
                    if user.second_app:
                        login(request, user)
                        messages.success(request, "Login successful", extra_tags="alert-success")
                        return redirect('base:home')
                    else:
                        user_profile = UserProfile.objects.get(user=user)
                        user_profile.account_balance += 500
                        user.second_app = True
                        user.save()
                        user_profile.save()
                        login(request, user)
                        messages.success(request, "Login successful", extra_tags="alert-success")
                        return redirect('base:home')
                else:
                    messages.error(request, "Your account is not activated", extra_tags="alert-danger")
            else:
                messages.error(request, "Invalid email/password", extra_tags="alert-danger")
    context = {
        'form': login_form
    }
    return render(request,"login.html", context)

def third_login(request):
    if request.user.is_authenticated:
        return redirect("base:home")
    login_form = LoginForm()
    if request.method == "POST":
        login_form = LoginForm(data=request.POST)
        if login_form.is_valid():
            email = request.POST["email"]
            password = request.POST["password"]
            user = authenticate(username=email, password=password)
            if user:
                if user.is_active:
                    if user.third_app:
                        login(request, user)
                        messages.success(request, "Login successful", extra_tags="alert-success")
                        return redirect('base:home')
                    else:
                        user_profile = UserProfile.objects.get(user=user)
                        user_profile.account_balance += 500
                        user.third_app = True
                        user.save()
                        user_profile.save()
                        login(request, user)
                        messages.success(request, "Login successful", extra_tags="alert-success")
                        return redirect('base:home')
                else:
                    messages.error(request, "Your account is not activated", extra_tags="alert-danger")
            else:
                messages.error(request, "Invalid email/password", extra_tags="alert-danger")
    context = {
        'form': login_form
    }
    return render(request,"login.html", context)


def fourth_login(request):
    if request.user.is_authenticated:
        return redirect("base:home")
    login_form = LoginForm()
    if request.method == "POST":
        login_form = LoginForm(data=request.POST)
        if login_form.is_valid():
            email = request.POST["email"]
            password = request.POST["password"]
            user = authenticate(username=email, password=password)
            if user:
                if user.is_active:
                    if user.fourth_app:
                        login(request, user)
                        messages.success(request, "Login successful", extra_tags="alert-success")
                        return redirect('base:home')
                    else:
                        user_profile = UserProfile.objects.get(user=user)
                        user_profile.account_balance += 500
                        user.fourth_app = True
                        user.save()
                        user_profile.save()
                        login(request, user)
                        messages.success(request, "Login successful", extra_tags="alert-success")
                        return redirect('base:home')
                else:
                    messages.error(request, "Your account is not activated", extra_tags="alert-danger")
            else:
                messages.error(request, "Invalid email/password", extra_tags="alert-danger")
    context = {
        'form': login_form
    }
    return render(request,"login.html", context)

def signup(request):
    if request.user.is_authenticated:
        return redirect("base:home")
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
                    messages.error(request, "Invalid user", extra_tags="alert-danger")
            except get_user_model().DoesNotExist:
                messages.error(request, "Referral not found", extra_tags="alert-danger")
            
            login(request, user)
            messages.success(request, "Login successful", extra_tags="alert-success")
            return redirect("base:home")
        else:
            messages.error(request, "Something went wrong, please try again", extra_tags="alert-danger")

            
            # messages.success(request, "Registration successful." )
        # messages.error(request, "Unsuccessful registration. Invalid information.")
    context = {
        'form': form
    }
    return render(request,"register.html", context)


@login_required(login_url="/")
def logout_view(request):
    logout(request)
    return redirect("/")

@login_required(login_url="/")
def home(request):

    context = {}
    return render(request,"dashboard.html", context)

@login_required(login_url="/")
def withdraw(request):
    withdrawals = Transactions.objects.filter(user=request.user, type="W")
    user_profile = UserProfile.objects.get(user=request.user)
    prev_trans = Transactions.objects.filter(user=request.user, type="W", status__in=["P", "PC"])
    form= WithdrawalForm()
    coupon_form = CouponForm()
    
    if request.method == "POST":
        form= WithdrawalForm(request.POST)
        coupon_form = CouponForm(request.POST)
        if coupon_form.is_valid():
            code = coupon_form.cleaned_data.get("code")
            coupon = Coupon.objects.filter(code=code)
            if coupon.exists():
                request.user.is_vip = True
                request.user.save()
                messages.success(request, "VIP badge pruchase successful", extra_tags="alert-success")
            else:
                messages.error(request, "Invalid coupon code", extra_tags="alert-danger")
                
                
            
        
        
        if form.is_valid():
            amount = form.cleaned_data.get("amount")
            balance = user_profile.account_balance

            if int(amount) > int(balance):
                messages.error(request, "You can not withdraw more than your balance", extra_tags="alert-danger")
            elif int(amount) < 4000:
                messages.error(request, "Minimum withdrawal is 4000 Naira", extra_tags="alert-danger")

            else:
                if prev_trans.exists():
                    messages.error(request, "You have a pending transaction, Please wait till it has been approved before making another withdrawal.", extra_tags="alert-danger")

                else:
                    if request.user.is_vip:
                        Transactions.objects.create(user=request.user, type="W", status="P", amount=amount, balance=int(balance)-int(amount))
                        messages.success(request, "Your withdrawal request has been successfully initiated, please wait for it to be processed", extra_tags="alert-success")
                    else:
                        percent = int(0.2 * amount)
                        Transactions.objects.create(user=request.user, type="W", status="P", amount=percent, balance=int(balance)-int(percent))
                        messages.success(request, "Your withdrawal request has been successfully initiated, please wait for it to be processed", extra_tags="alert-success")
                 
    form= WithdrawalForm()



    context = {
        "withdrawals" :  withdrawals,
        "form" :  form,
        "coupon_form": coupon_form
        }
    return render(request,"withdraw.html", context)

@login_required(login_url="/")
def profile(request):
    context = {}
    return render(request,"profile.html", context)

@login_required(login_url="/")
def how(request):
    context = {}
    return render(request,"how-to.html", context)

@login_required(login_url="/")
def tasks(request):
    context = {}
    return render(request,"tasks.html", context)

@login_required(login_url="/")
def delete_withdrawal(request, id):
    trans = Transactions.objects.get(id=id)
    messages.success(
        request, f"Transaction deleted", extra_tags="alert-success")
    trans.delete()
    return redirect("base:withdraw")

@login_required(login_url="/")
def referrals(request):
    referrals_count = Referral.objects.filter(referrer=request.user.profile).count()
    context = {
        "referrals_count": referrals_count,
        
        }
    return render(request,"referral.html", context)
