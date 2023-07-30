from django.shortcuts import render, redirect
from authentication.forms import LoginForm
from django.contrib.auth import authenticate, login

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


def home(request):
    return render(request,"dashboard.html")