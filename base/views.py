from django.shortcuts import render, redirect
from account.models import Bank, Coupon, Referral, Transactions, UserProfile
from authentication.forms import BankForm, CouponForm, LoginForm, NewUserForm, WithdrawalForm
from django.contrib.auth import authenticate, login, logout
from django.db.models import Sum
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import FileResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404
from django.views import View
import os
from django.conf import settings



class successMessage(SuccessMessageMixin):
    
    def form_valid(self, form):
        response = super().form_valid(form)
        success_message = self.get_success_message(form.cleaned_data)
        if success_message:
            messages.success(self.request, success_message, extra_tags='alert alert-success')
        return response
    

# Create your views here.

class ResetPasswordView(successMessage, PasswordResetView):
    template_name = 'password_reset.html'
    email_template_name = 'password_reset_email.html'
    subject_template_name = 'password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('base:login')
    
    
    
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
                messages.success(request, "VIP badge purchase successful", extra_tags="alert-success")
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
                        percent = 0.2 * int(amount)
                        print(percent, 'percent', amount, 'amount')
                        Transactions.objects.create(user=request.user, type="W", status="P", amount=percent, balance=int(balance)-int(percent))
                        messages.success(request, "Your withdrawal request has been successfully initiated, please wait for it to be processed", extra_tags="alert-success")
                 
    else:
        form= WithdrawalForm()
        coupon_form = CouponForm()



    context = {
        "withdrawals" :  withdrawals,
        "form" :  form,
        "coupon_form": coupon_form
        }
    return render(request,"withdraw.html", context)

@login_required(login_url="/")
def profile(request):
    bank = Bank.objects.get(user=request.user)
    form = BankForm(instance=bank)
    if request.method == 'POST':
        form = BankForm(instance=bank, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Bank account updated successfully", extra_tags="alert-success")
        else:
            messages.error(request, "Something went wrong, please try again", extra_tags="alert-danger")
    context = {
        'form': form
    }
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

def privacy(request):
    # referrals_count = Referral.objects.filter(referrer=request.user.profile).count()
    context = {
        # "referrals_count": referrals_count,
        
        }
    return render(request,"privacy.html", context)


class FileDownloadView(View):
    def get(self, request, file_name):
        # Specify the path to your file in the base folder
        file_path = os.path.join(settings.BASE_DIR, file_name)
        print(file_path)
        
        # Check if the file exists
        if os.path.exists(file_path):
            # Create a FileResponse directly without manually opening the file
            response = FileResponse(open(file_path, 'rb'))
            # Set the content type for the response to APK
            response['content_type'] = 'application/vnd.android.package-archive'
            # Set the Content-Disposition header to force download
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
            return response
        else:
            # Return a 404 response if the file does not exist
            return get_object_or_404(HttpResponseNotFound)